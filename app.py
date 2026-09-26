import streamlit as st
import pandas as pd
import plotly.express as px

# Глобальная настройка страницы в темной премиум палитре
st.set_page_config(page_title="AI Anti-Fraud Hub — Team C1094BD7", layout="wide", initial_sidebar_state="collapsed")

# Внедрение кастомного CSS для интерактивного неонового свечения карточек участников при наведении
st.markdown("""
<style>
    /* Базовая настройка стандартных навигационных вкладок Streamlit */
    button[data-baseweb='tab'] {
        color: #8892B0 !important;
        font-size: 15px !important;
        font-weight: 600 !important;
    }
    button[data-baseweb='tab'][aria-selected='true'] {
        color: #0070C0 !important;
    }
    
    /* Изолированные CSS стили для красивых заблюренных неоновых карточек участников */
    .fbu-custom-card {
        background: rgba(23, 42, 69, 0.45) !important;
        border: 1px solid rgba(0, 112, 192, 0.25) !important;
        border-radius: 16px !important;
        padding: 35px 20px !important;
        box-shadow: 0 8px 25px rgba(0,0,0,0.4) !important;
        text-align: center !important;
        transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
        flex: 1;
    }
    
    /* АНИМАЦИЯ: Эффект парения и сочного неонового свечения строго при наведении мыши на карточку инфо */
    .fbu-custom-card:hover {
        transform: translateY(-8px) scale(1.02) !important;
        border-color: #38EF7D !important; /* Рамка зажигается неоново-зеленым */
        box-shadow: 0 0 35px rgba(56, 239, 125, 0.4), 0 15px 40px rgba(0, 0, 0, 0.6) !important; /* Плотное зеленое свечение */
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# APPLICATION HEADING - TOP LEVEL BRANDING NODE (ВШИТЫЙ ЛОГОТИП СВЕРХУ ПО ЦЕНТРУ)
# ==============================================================================
# Оригинальный логотип FBU переведен в Base64 для 100% стабильного отображения в облаке без значка Zoom
st.markdown("""
<center>
    <img src="data:image/jpeg;base64,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" 
         width="165" 
         style="border-radius:14px; box-shadow:0 6px 22px rgba(0,112,192,0.35); margin-top:10px; margin-bottom:15px; pointer-events:none;">
</center>
""", unsafe_allow_html=True)

st.title("🛡️ NEXUS: Next-Gen AI Anti-Fraud Analytics Platform")
st.subheader("Advanced Financial Monitoring System | Powered by Team C1094BD7")

st.markdown("<div style='background:rgba(0,112,192,0.1);border-left:4px solid #0070C0;padding:15px;border-radius:4px;margin-bottom:25px;'><strong>Global Operational Status:</strong> Standing at the intersection of Big Data and Cybersecurity. Our neural-gradient framework dissects financial transaction patterns in real-time, isolating high-risk threats from millions of safe everyday operations.</div>", unsafe_allow_html=True)

# Создание 4 стандартных вкладок навигации в самом верху страницы
tab1, tab2, tab3, tab4 = st.tabs(["🚀 Core Architecture", "📊 Live Metrics Hub", "🏆 Machine Learning Logic", "🏢 About FBU"])

# ==============================================================================
# TAB 1: CORE ARCHITECTURE
# ==============================================================================
with tab1:
    st.write("### Intelligent Threat Filtering Ecosystem")
    st.markdown("In high-volume banking sectors, compliance departments face an informational avalanche — hundreds of thousands of daily automated system flags. Reviewing every alert manually compromises security response times and burns critical human resources. **Our Solution:** We constructed an end-to-end analytical core that ingests raw, relational historical transaction databases. By converting raw money movements into structured behavior maps, the AI instantly computes an escalation probability score.")
    st.write("---")
    st.write("### 🔍 Feature Engineering & Behavioral Pillars")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        with st.expander("💸 1. Capital Velocity & Drainage"):
            st.write("Rapid fund rotation. If an account receives a major credit placement (Kirim) and mirrors it via multiple outbound transfers (Chiqim) within a tight time-window, the AI flags classic money-laundering transit behavior.")
    with col2:
        with st.expander("🌍 2. Cross-Border Channel Friction"):
            st.write("Sudden geographical shifts. When historical spending patterns rooted heavily in local domestic systems switch instantly to high-volume international wires (Xalqaro), the risk weight mutates to Maximum.")
    with col3:
        with st.expander("📈 3. Volatility & Deviation Spikes"):
            st.write("Absolute sum mutation. The framework tracks rolling behavioral baselines. A transaction that severely overshoots a customer's standard deviation index triggers immediate automated containment.")

# ==============================================================================
# TAB 2: LIVE METRICS HUB
# ==============================================================================
with tab2:
    st.write("### 📊 Macro-Data Stream Summary")
    st.write("#### 📈 Deep Data Processing Volumes")
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric(label="Total Transaction Records Processed", value="694,094 rows", delta="Train + Test Batches")
    with c2:
        st.metric(label="Mean Transaction Amount", value="42.53K UZS", delta="+1.24% Vs Baseline")
    with c3:
        st.metric(label="Automated False Alarm Suppression", value="92.31%", delta="Operational Noise Cut", delta_color="inverse")
    with c4:
        st.metric(label="Escalated High-Priority Targets", value="7.69%", delta="Verified Risk Signals")

    st.write("---")
    st.write("#### 💳 Channel Throughput & Volume Allocation")
    
    col_a, col_b, col_c, col_d = st.columns(4)
    with col_a:
        st.metric(label="International Wires (Xalqaro)", value="142.54M UZS", delta="Critical Exposure Level")
    with col_b:
        st.metric(label="Card Operations (Karta)", value="310.21M UZS", delta="Highest Volume Channel")
    with col_c:
        st.metric(label="Cash Dispersals (Naqd)", value="85.08M UZS", delta="Minimal Risk Footprint")
    with col_d:
        st.metric(label="Interbank Settlements (O'tkazma)", value="156.26M UZS", delta="Standard Corporate Rate")

    st.write("---")
    left_col, right_col = st.columns(2)
    with left_col:
        st.write("### 🚨 The Imbalance Dilemma (Target Distribution)")
        target_data = pd.DataFrame({'Alert Vector': ['False Alarm (Dismissed)', 'Genuine Threat (Escalated)'], 'Volume': [92.31, 7.69]})
        fig_target = px.pie(target_data, values='Volume', names='Alert Vector', hole=0.5, color_discrete_sequence=['#172A45', '#0070C0'])
        fig_target.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#F8F9FA')
        
