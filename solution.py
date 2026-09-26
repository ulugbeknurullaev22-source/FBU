import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import roc_auc_score
import warnings
warnings.filterwarnings('ignore')

TEAM_ID = "C1094BD7"

# Шаг 1: Загрузка основных сигналов алертов
train_signals = pd.read_csv('train_signals.csv')
test_signals = pd.read_csv('test_signals.csv')

# Шаг 2: Загрузка транзакционных Parquet-файлов histories
train_tx = pd.read_parquet('train_transactions.parquet')
test_tx = pd.read_parquet('test_transactions.parquet')

def advanced_feature_engineering(df_tx):
    # Функция агрегации реляционных транзакционных данных по signal_id
    
    # 1. Агрегаты по стандартизированным объемам транзакций
    features = df_tx.groupby('signal_id')['miqdor_indeksi'].agg([
        'count', 'sum', 'mean', 'max', 'std', 'min'
    ]).reset_index()
    features.columns = ['signal_id', 'tx_count', 'tx_sum', 'tx_mean', 'tx_max', 'tx_std', 'tx_min']
    
    # 2. Определение направления потоков (выявление транзитных транзакций)
    df_tx['is_kirim'] = (df_tx['kirim_chiqim'] == 'kirim').astype(int)
    df_tx['is_chiqim'] = (df_tx['kirim_chiqim'] == 'chiqim').astype(int)
    
    direction_stats = df_tx.groupby('signal_id').agg({
        'is_kirim': 'sum',
        'is_chiqim': 'sum'
    }).reset_index()
    
    direction_stats['kirim_ratio'] = direction_stats['is_kirim'] / (direction_stats['is_kirim'] + direction_stats['is_chiqim'] + 1e-5)
    features = pd.merge(features, direction_stats[['signal_id', 'kirim_ratio']], on='signal_id', how='left')
    
    # 3. Раздельный анализ структуры типов транзакций
    for tx_type in ['karta', 'naqd', 'xalqaro', 'bank_otkazmasi']:
        df_tx[f'amt_{tx_type}'] = np.where(df_tx['tranzaksiya_turi'] == tx_type, df_tx['miqdor_indeksi'], 0)
        df_tx[f'cnt_{tx_type}'] = np.where(df_tx['tranzaksiya_turi'] == tx_type, 1, 0)
        
    type_aggs = df_tx.groupby('signal_id').agg({
        'amt_karta': 'sum', 'cnt_karta': 'sum',
        'amt_naqd': 'sum', 'cnt_naqd': 'sum',
        'amt_xalqaro': 'sum', 'cnt_xalqaro': 'sum',
        'amt_bank_otkazmasi': 'sum', 'cnt_bank_otkazmasi': 'sum'
    }).reset_index()
    
    features = pd.merge(features, type_aggs, on='signal_id', how='left')
    return features

# Извлечение признаков
train_features = advanced_feature_engineering(train_tx)
test_features = advanced_feature_engineering(test_tx)

train_df = pd.merge(train_signals, train_features, on='signal_id', how='left')
test_df = pd.merge(test_signals, test_features, on='signal_id', how='left')

train_df.fillna(0, inplace=True)
test_df.fillna(0, inplace=True)

# Шаг 3: Временные фичи и хронологическая сортировка во избежание data leakage
for df in [train_df, test_df]:
    df['signal_sanasi'] = pd.to_datetime(df['signal_sanasi'])
    df['month'] = df['signal_sanasi'].dt.month
    df['dayofweek'] = df['signal_sanasi'].dt.dayofweek

train_df = train_df.sort_values('signal_sanasi').reset_index(drop=True)

exclude_cols = ['signal_id', 'signal_sanasi', 'eskalatsiya']
feature_cols = [col for col in train_df.columns if col not in exclude_cols]

X = train_df[feature_cols]
y = train_df['eskalatsiya']
X_test = test_df[feature_cols]

# Шаг 4: Кросс-валидация TimeSeriesSplit и обучение LightGBM
ts_split = TimeSeriesSplit(n_splits=5)
test_preds = np.zeros(len(test_df))

# Корректировка баланса классов несбалансированной выборки финмониторинга
scale_weight = (len(y) - sum(y)) / sum(y)

params = {
    'objective': 'binary',
    'metric': 'auc',
    'boosting_type': 'gbdt',
    'learning_rate': 0.03,
    'num_leaves': 31,
    'max_depth': 6,
    'feature_fraction': 0.75,
    'scale_pos_weight': scale_weight,
    'verbose': -1,
    'random_state': 42
}

for fold, (train_idx, val_idx) in enumerate(ts_split.split(X)):
    X_train, y_train = X.iloc[train_idx], y.iloc[train_idx]
    X_val, y_val = X.iloc[val_idx], y.iloc[val_idx]
    
    train_data = lgb.Dataset(X_train, label=y_train)
    val_data = lgb.Dataset(X_val, label=y_val, reference=train_data)
    
    model = lgb.train(
        params,
        train_data,
        num_boost_round=1500,
        valid_sets=[train_data, val_data],
        callbacks=[lgb.early_stopping(stopping_rounds=50, verbose=False)]
    )
    
    test_preds += model.predict(X_test, num_iteration=model.best_iteration) / ts_split.n_splits

# Шаг 5: Экспорт результатов согласно правилам оценивания (ROC-AUC)
submission = pd.DataFrame({
    'signal_id': test_signals['signal_id'],
    'ehtimollik': test_preds
})

submission.to_csv(f'team_{TEAM_ID}.csv', index=False)
print(f"Файл сохранен: team_{TEAM_ID}.csv")
