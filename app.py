import streamlit as st
import pandas as pd
import plotly.express as px

# Настройка страницы: деликатный темный режим без боковой панели
st.set_page_config(page_title="NEXUS AI — INHA Blue Edition", layout="wide", initial_sidebar_state="collapsed")

# Внедрение кастомного CSS для деликатного черного стиля, синего цвета ИНХА и размытых боксов
st.markdown("""
<style>
    /* Базовый деликатный черный фон (Matte Carbon Premium) */
    .stApp {
        background: #0B0C10 !important;
        color: #EAEAEA !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    /* Заголовки в фирменном синем цвете Университета ИНХА */
    h1 {
        color: #FFFFFF !important;
        font-weight: 800 !important;
        font-size: 2.8rem !important;
        letter-spacing: -0.5px;
        text-shadow: 0px 4px 15px rgba(0, 82, 155, 0.3);
    }
    h2, h3 {
        color: #00529B !important; /* INHA Blue */
        font-weight: 700 !important;
    }
    
    /* Центрирование и увеличение вкладок-кнопок */
    div[data-baseweb="tab-list"] {
        display: flex !important;
        gap: 25px !important;
        justify-content: center !important; /* Вкладки строго по центру */
        margin-bottom: 45px !important;
        background: transparent !important;
        border: none !important;
        width: 100% !important;
    }
    
    /* Превращаем стандартные вкладки в БОЛЬШИЕ КНОПКИ */
    button[data-baseweb="tab"] {
        background: #1F2833 !important;
        border: 2px solid rgba(0, 82, 155, 0.3) !important;
        border-radius: 12px !important;
        color: #C5C6C7 !important;
        padding: 18px 45px !important;
        font-size: 18px !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px;
        transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1) !important;
        cursor: pointer !important;
    }
    
    /* АНИМАЦИЯ: Эффект нажатия и неоновое синее свечение при наведении на кнопки */
    button[data-baseweb="tab"]:hover {
        color: #FFFFFF !important;
        background: #141A22 !important;
        border-color: #00529B !important;
        transform: translateY(-3px) !important;
        box-shadow: 0 0 20px rgba(0, 82, 155, 0.4) !important;
    }
    
    /* Стиль для активной (выбранной) огромной кнопки */
    button[data-baseweb="tab"][aria-selected="true"] {
        background: #00529B !important; /* Цвет ИНХА */
        color: #FFFFFF !important;
        border-color: #00529B !important;
        box-shadow: 0 0 25px rgba(0, 82, 155, 0.6) !important;
        transform: scale(1.03) !important;
    }
    
    /* РАЗМЫТИЕ СТАТИСТИКИ (Glassmorphism Box-Shadow Blur) */
    div[data-testid="stMetric"], .streamlit-expanderHeader {
        background: rgba(31, 40, 51, 0.4) !important;
        backdrop-filter: blur(20px) opacity(1) !important; /* Сильное размытие заднего плана */
        -webkit-backdrop-filter: blur(20px) !important;
        border: 1px solid rgba(0, 82, 155, 0.2) !important;
        border-radius: 16px !important;
        padding: 25px !important;
        /* Тень, которая выталкивает бокс из бэкграунда и заставляет его выделяться */
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.6), 0 0 15px rgba(0, 82, 155, 0.1) !important;
        transition: all 0.3s ease !important;
    }
    
    /* Плавная анимация парения карточки при наведении */
    div[data-testid="stMetric"]:hover {
        transform: translateY(-6px) !important;
        border-color: #00529B !important;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.7), 0 0 25px rgba(0, 82, 155, 0.3) !important;
    }
    
    /* Отключение дефолтных полос под вкладками */
    div[data-baseweb="tab-highlight-id"] {
        background-color: transparent !important;
    }
</style>
""", unsafe_allow_html=True)

# Главный блок заголовка
st.title("🛡️ NEXUS ANTI-FRAUD")
st.markdown("<p style='color:#C5C6C7; font-size:16px; margin-top:-10px;'>Advanced Financial Monitoring System | Powered by Team C1094BD7</p>", unsafe_allow_html=True)

st.write("---")

# Огромные кнопки-вкладки строго по центру экрана
tab1, tab2, tab3 = st.tabs(["🚀 ARCHITECTURE", "📊 METRICS HUB", "🏆 AI LOGIC"])

# ==============================================================================
# ВКЛАДКА 1: ARCHITECTURE
# ==============================================================================
with tab1:
    st.write("### Shifting From Manual Review to High-Speed AI")
    st.markdown("""
    In high-volume banking sectors, compliance departments face **an informational avalanche** — hundreds of thousands of daily automated system flags. 
    Reviewing every alert manually compromises security response times and burns critical human resources.

    **Our Solution:** 
    We constructed an end-to-end analytical core that ingests raw, relational historical transaction databases. 
    By converting raw money movements into structured behavior maps, the AI instantly computes an escalation probability score. 
    Analysts no longer search blindly; they address highest-probability threats first.
    """)

    st.write("---")
    st.write("### 🔍 Core Behavioral Anomalies Found")
    st.markdown("Click to expand our data investigation nodes:")

    col1, col2, col3 = st.columns(3)
    with col1:
        with st.expander("💸 1. Capital Velocity & Drainage"):
            st.write("Rapid fund rotation. If an account receives a major credit placement (Kirim) and mirrors it via multiple outbound transfers (Chiqim) within a tight time-window, the AI flags classic money-laundering transit behavior.")
    with col2:
        with st.expander("🌍 2. Cross-Border Channels"):
            st.write("Sudden geographical shifts. When historical spending patterns rooted heavily in local domestic systems (Tashkent retail) switch instantly to high-volume international wires (Xalqaro), the risk weight mutates to Maximum.")
    with col3:
        with st.expander("📈 3. Volatility Spikes"):
            st.write("Absolute sum mutation. The framework tracks rolling behavioral baselines. A transaction that severely overshoots a customer's standard deviation index triggers immediate automated containment.")

# ==============================================================================
# ВКЛАДКА 2: METRICS HUB (ЗАБЛЮРЕННЫЕ БОКСЫ И СТАТИСТИКА)
# ==============================================================================
with tab2:
    st.write("### 📊 Macro-Data Stream Summary")
    st.markdown("*Hover over the glassmorphic metric cards to test the smooth blur and box-shadow depth scaling:*")
    
    st.write("#### 📈 Deep Data Processing Volumes")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric(label="Total Transactions Processed", value="694,094 rows", delta="Train + Test Batches")
    with c2:
        st.metric(label="Mean Transaction Index Metric", value="42.53 Index", delta="+1.24% Vs Baseline")
    with c3:
        st.metric(label="Automated False Alarm Suppression", value="92.31%", delta="Operational Noise Cut", delta_color="inverse")
    with c4:
        st.metric(label="Escalated High-Priority Targets", value="7.69%", delta="Verified Risk Signals")

    st.write("---")
    
    st.write("#### 💳 Channel Throughput & Risk Allocations")
    col_a, col_b, col_c, col_d = st.columns(4)
    with col_a:
        st.metric(label="International Wires (Xalqaro)", value="142.54M Index", delta="Critical Exposure Level")
    with col_b:
        st.metric(label="Card Operations (Karta)", value="310.21M Index", delta="Highest Volume Channel")
    with col_c:
        st.metric(label="Cash Dispersals (Naqd)", value="85.08M Index", delta="Minimal Risk Footprint")
    with col_d:
        st.metric(label="Interbank Settlements (O'tkazma)", value="156.26M Index", delta="Standard Corporate Rate")

    st.write("---")
    
    # Распределения графиков в глубокой синей гамме INHA
    left_col, right_col = st.columns(2)
    with left_col:
        st.write("### 🚨 The Imbalance Dilemma (Target Distribution)")
        target_data = pd.DataFrame({
            'Alert Vector': ['False Alarm (Dismissed)', 'Genuine Threat (Escalated)'], 
            'Volume': [320000, 26948]
        })
        fig_target = px.pie(target_data, values='Volume', names='Alert Vector', 
                            color_discrete_sequence=['#1F2833', '#00529B'])
        fig_target.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#EAEAEA')
        st.plotly_chart(fig_target, use_container_width=True)

    with right_col:
        st.write("### ✈️ Operational Risk Conversion by Medium")
        type_data = pd.DataFrame({
            'Medium': ['Cards', 'Cash', 'International', 'Bank Transfer'],
            'Risk Density (%)': [8.2, 4.1, 38.5, 12.3]
        })
        fig_type = px.bar(type_data, x='Medium', y='Risk Density (%)', text_auto=True,
                          color='Risk Density (%)', color_continuous_scale=['#1F2833', '#00529B'])
        fig_type.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#EAEAEA')
        st.plotly_chart(fig_type, use_container_width=True)

# ==============================================================================
# ВКЛАДКА 3: MACHINE LEARNING LOGIC
# ==============================================================================
with tab3:
    st.write("### 🏆 Mathematical Decision Architecture")
    st.markdown("Transparency is vital for modern banking operations. Below is the strict information gain metrics computed by our **LightGBM** core.")
    
    st.write("#### 🎯 Feature Importance Vectors (Top 3 Performance Drivers)")
    rf1, rf2, rf3 = st.columns(3)
    with rf1:
        st.markdown("#### 🥇 Peak Single Volume (`tx_max`)")
        st.metric(label="Information Gain Weight", value="432.50", delta="Primary Splitting Node")
