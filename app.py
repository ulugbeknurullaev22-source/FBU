import streamlit as st
import pandas as pd
import plotly.express as px

# Настройка страницы: темная тема и убираем боковое меню для фокуса на дизайне
st.set_page_config(page_title="NEXUS AI — Team C1094BD7", layout="wide", initial_sidebar_state="collapsed")

# Внедрение мощного кастомного CSS для премиум-дизайна и анимаций
st.markdown("""
<style>
    /* Главный фон в стиле глубокого угольного премиум-дарк мода */
    .stApp {
        background: linear-gradient(180deg, #0D0F14 0%, #171B22 100%) !important;
        color: #F8F9FA !important;
        font-family: 'Inter', sans-serif !important;
    }

    .block-container {
        padding-top: 2.5rem !important;
        max-width: 1200px !important;
    }

    /* Hero-заголовок в духе референса: крупно, жирно, с акцентной плашкой */
    .hero-eyebrow {
        display: inline-block;
        color: #39FF14 !important;
        font-weight: 800;
        font-size: 13px;
        letter-spacing: 3px;
        text-transform: uppercase;
        background: rgba(57, 255, 20, 0.08);
        border: 1px solid rgba(57, 255, 20, 0.35);
        padding: 6px 16px;
        border-radius: 999px;
        margin-bottom: 14px;
    }

    h1 {
        color: #FFFFFF !important;
        font-weight: 900 !important;
        font-size: 3.4rem !important;
        line-height: 1.05 !important;
        letter-spacing: -1.5px;
        margin-bottom: 5px !important;
    }
    h2, h3 {
        color: #39FF14 !important; /* Яркий неоново-зеленый (Cyber Lime) как на референсе */
        font-weight: 700 !important;
    }

    /* ===== ВКЛАДКИ: большие круглые "кнопки" по центру, как пилюли на референсе ===== */
    div[data-baseweb="tab-list"] {
        display: flex !important;
        gap: 24px !important;
        justify-content: center !important;
        align-items: center !important;
        margin: 10px 0 48px 0 !important;
        background: transparent !important;
        border: none !important;
        flex-wrap: wrap;
    }

    button[data-baseweb="tab"] {
        background: rgba(29, 36, 45, 0.7) !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(57, 255, 20, 0.18) !important;
        border-radius: 999px !important;
        color: #8E9AA8 !important;
        padding: 26px 52px !important;
        min-height: unset !important;
        font-size: 22px !important;
        font-weight: 800 !important;
        text-transform: uppercase !important;
        letter-spacing: 1.5px;
        transition: all 0.35s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
        box-shadow: 0 4px 20px rgba(0,0,0,0.25) !important;
    }

    button[data-baseweb="tab"] p {
        font-size: 22px !important;
        font-weight: 800 !important;
    }

    /* АНИМАЦИЯ: Плавное увеличение и неоновая подсветка вкладок при наведении */
    button[data-baseweb="tab"]:hover {
        color: #FFFFFF !important;
        background: rgba(40, 50, 62, 0.9) !important;
        border-color: #39FF14 !important;
        transform: scale(1.06) translateY(-3px) !important;
        box-shadow: 0 0 30px rgba(57, 255, 20, 0.35) !important;
    }

    /* Стиль для активной (выбранной в данный момент) огромной вкладки */
    button[data-baseweb="tab"][aria-selected="true"] {
        background: #39FF14 !important;
        color: #11141A !important;
        border-color: #39FF14 !important;
        box-shadow: 0 0 40px rgba(57, 255, 20, 0.55) !important;
        transform: scale(1.03) !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] p {
        color: #11141A !important;
    }

    /* Убираем стандартные подчеркивания Streamlit под вкладками */
    div[data-baseweb="tab-highlight-id"], div[data-baseweb="tab-border"] {
        background-color: transparent !important;
    }

    /* ===== Карточки-иконки в духе референса (круглый значок + подпись) ===== */
    .feature-card {
        background: rgba(24, 31, 39, 0.6);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255,255,255,0.05);
        border-radius: 18px;
        padding: 28px 20px;
        text-align: center;
        transition: all 0.3s ease;
    }
    .feature-card:hover {
        transform: translateY(-8px);
        border-color: rgba(57,255,20,0.4);
        box-shadow: 0 15px 40px rgba(57,255,20,0.15);
    }
    .feature-icon {
        width: 56px; height: 56px;
        border-radius: 50%;
        background: rgba(57,255,20,0.1);
        border: 1px solid rgba(57,255,20,0.4);
        display: flex; align-items: center; justify-content: center;
        font-size: 24px;
        margin: 0 auto 14px auto;
    }
    .feature-label {
        color: #F8F9FA;
        font-weight: 700;
        font-size: 15px;
        letter-spacing: 0.5px;
    }

    /* Стилизация информационных карточек-метрик (Glassmorphism с размытием) */
    div[data-testid="stMetric"], .streamlit-expanderHeader {
        background: rgba(24, 31, 39, 0.6) !important;
        backdrop-filter: blur(15px) !important;
        -webkit-backdrop-filter: blur(15px) !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
        border-radius: 16px !important;
        padding: 25px !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4) !important;
        transition: all 0.3s ease !important;
    }

    /* АНИМАЦИЯ: Эффект парения карточек статистики при наведении */
    div[data-testid="stMetric"]:hover {
        transform: translateY(-8px) !important;
        border-color: rgba(57, 255, 20, 0.4) !important;
        box-shadow: 0 15px 40px rgba(57, 255, 20, 0.15) !important;
    }
</style>
""", unsafe_allow_html=True)

# Верхний баннер сайта
st.markdown("<div class='hero-eyebrow'>Stay Secure & Sharp</div>", unsafe_allow_html=True)
st.title("🛡️ NEXUS ANTI-FRAUD")
st.markdown("<p style='color:#8E9AA8; font-size:18px; margin-top:-10px;'>Advanced Financial Monitoring System | Team C1094BD7</p>", unsafe_allow_html=True)

st.write("---")

# Создаем огромные интерактивные вкладки-кнопки по центру экрана
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

    # Карточки-иконки в стиле референса ("Make Your Body Harmonic" и т.д.)
    fc1, fc2, fc3 = st.columns(3)
    with fc1:
        st.markdown("""
        <div class='feature-card'>
            <div class='feature-icon'>💸</div>
            <div class='feature-label'>Cash Out Velocity</div>
        </div>
        """, unsafe_allow_html=True)
    with fc2:
        st.markdown("""
        <div class='feature-card'>
            <div class='feature-icon'>🌍</div>
            <div class='feature-label'>Cross-Border Channels</div>
        </div>
        """, unsafe_allow_html=True)
    with fc3:
        st.markdown("""
        <div class='feature-card'>
            <div class='feature-icon'>📈</div>
            <div class='feature-label'>Volatility Spikes</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("Click to expand our data investigation nodes:")
    col1, col2, col3 = st.columns(3)
    with col1:
        with st.expander("💸 1. Cash Out Velocity"):
            st.write("Rapid fund rotation. If an account receives a major credit placement (Kirim) and mirrors it via multiple outbound transfers (Chiqim) within a tight time-window, the AI flags classic money-laundering transit behavior.")
    with col2:
        with st.expander("🌍 2. Cross-Border Channels"):
            st.write("Sudden geographical shifts. When historical spending patterns rooted heavily in local domestic systems (Tashkent retail) switch instantly to high-volume international wires (Xalqaro), the risk weight mutates to Maximum.")
    with col3:
        with st.expander("📈 3. Volatility Spikes"):
            st.write("Absolute sum mutation. The framework tracks rolling behavioral baselines. A transaction that severely overshoots a customer's standard deviation index triggers immediate automated containment.")

# ==============================================================================
# ВКЛАДКА 2: METRICS HUB (КАРТОЧКИ С АНИМАЦИЕЙ)
# ==============================================================================
with tab2:
    st.write("### 📊 Macro-Data Stream Summary")
    st.markdown("*Hover over the glassmorphic metric cards to test the smooth scaling animation:*")
    
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
    
    # Графики в темной палитре
    left_col, right_col = st.columns(2)
    with left_col:
        st.write("### 🚨 The Imbalance Dilemma (Target Distribution)")
        target_data = pd.DataFrame({
            'Alert Vector': ['False Alarm (Dismissed)', 'Genuine Threat (Escalated)'], 
            'Volume': [320000, 26948]
        })
        fig_target = px.pie(target_data, values='Volume', names='Alert Vector', 
                            color_discrete_sequence=['#1D242D', '#39FF14'])
        fig_target.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#F8F9FA')
        st.plotly_chart(fig_target, use_container_width=True)

    with right_col:
        st.write("### ✈️ Operational Risk Conversion by Medium")
        type_data = pd.DataFrame({
            'Medium': ['Cards', 'Cash', 'International', 'Bank Transfer'],
            'Risk Density (%)': [8.2, 4.1, 38.5, 12.3]
        })
        fig_type = px.bar(type_data, x='Medium', y='Risk Density (%)', text_auto=True,
                          color='Risk Density (%)', color_continuous_scale=['#1D242D', '#39FF14'])
        fig_type.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#F8F9FA')
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
        st.caption("Sudden massive capital spikes diverge violently from historical retail baselines.")
    with rf2:
        st.markdown("#### 🥈 Liquidation Velocity (`kirim_ratio`)")
