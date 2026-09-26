import streamlit as st
import pandas as pd
import plotly.express as px

# Глобальная настройка страницы
st.set_page_config(page_title="AI Anti-Fraud Hub — Team C1094BD7", layout="wide", initial_sidebar_state="collapsed")

# Безопасный CSS только для кастомизации дефолтных вкладок (не трогает другие блоки)
st.markdown("""
<style>
    button[data-baseweb='tab'] {
        color: #8892B0 !important;
        font-size: 15px !important;
        font-weight: 600 !important;
    }
    button[data-baseweb='tab'][aria-selected='true'] {
        color: #0070C0 !important;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# APPLICATION HEADING - TOP LEVEL BRANDING NODE (СВЕРХУ ПО СЕРЕДИНЕ)
# ==============================================================================
st.markdown("<center><img src='https://githubusercontent.com' width='180' style='border-radius:12px;box-shadow:0 4px 20px rgba(0,112,192,0.3);margin-top:10px;margin-bottom:15px;pointer-events:none;'></center>", unsafe_allow_html=True)

st.title("🛡️ NEXUS: Next-Gen AI Anti-Fraud Analytics Platform")
st.subheader("Advanced Financial Monitoring System | Powered by Team C1094BD7")

st.markdown("<div style='background:rgba(0,112,192,0.1);border-left:4px solid #0070C0;padding:15px;border-radius:4px;margin-bottom:25px;'><strong>Global Operational Status:</strong> Standing at the intersection of Big Data and Cybersecurity. Our neural-gradient framework dissects financial transaction patterns in real-time, isolating high-risk threats from millions of safe everyday operations.</div>", unsafe_allow_html=True)

# Generate functional top-level navigation tabs
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
    st.title("🛡️ NEXUS: Next-Gen AI Anti-Fraud Analytics Platform")
    st.subheader("Advanced Financial Monitoring System | Powered by Team C1094BD7")
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
        st.plotly_chart(fig_target, use_container_width=True, config={'displayModeBar': False})

    with right_col:
        st.write("### ✈️ Operational Risk Conversion by Medium")
        type_data = pd.DataFrame({'Medium': ['Cards', 'Cash', 'International', 'Bank Transfer'], 'Risk Density (%)': [8.2, 4.1, 38.5, 12.3]})
        fig_type = px.bar(type_data, x='Medium', y='Risk Density (%)', text_auto=True, color='Risk Density (%)', color_continuous_scale=['#172A45', '#0070C0'])
        fig_type.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#F8F9FA', coloraxis_showscale=False, xaxis=dict(showgrid=False), yaxis=dict(showgrid=False, visible=False))
        st.plotly_chart(fig_type, use_container_width=True, config={'displayModeBar': False})

# ==============================================================================
# TAB 3: MACHINE LEARNING LOGIC
# ==============================================================================
with tab3:
    st.title("🛡️ NEXUS: Next-Gen AI Anti-Fraud Analytics Platform")
    st.subheader("Advanced Financial Monitoring System | Powered by Team C1094BD7")
    st.write("### 🏆 Mathematical Decision Architecture")
    st.write("#### 🎯 Feature Importance Vectors (Top 3 Performance Drivers)")
    
    rf1, rf2, rf3 = st.columns(3)
    with rf1:
        st.metric(label="🥇 Peak Single Volume (tx_max)", value="432.50", delta="Primary Splitting Node")
    with rf2:
        st.metric(label="🥈 Liquidation Velocity (kirim_ratio)", value="389.12", delta="Flow Balance Node")
    with rf3:
        st.metric(label="🥉 Cross-Border Intensity (amt_xalqaro)", value="295.41", delta="Compliance Node")

    st.write("---")
    st.write("#### Exhaustive Feature Contribution Graph")
    importance_data = pd.DataFrame({'Mathematical Dimension': ['Max Volume UZS (tx_max)', 'Flow Velocity (kirim_ratio)', 'International Wires UZS (amt_xalqaro)', 'Transaction Density (tx_count)', 'Sigma Volatility UZS (tx_std)', 'Card Aggregate UZS (amt_karta)', 'Temporal Vector (dayofweek)'], 'Gain Points': [432.5, 389.1, 295.4, 210.8, 185.3, 112.4, 45.2]})
    importance_data = importance_data.sort_values(by='Gain Points', ascending=True)

    fig_imp = px.bar(importance_data, x='Gain Points', y='Mathematical Dimension', orientation='h', text_auto=True, color='Gain Points', color_continuous_scale=['#172A45', '#0070C0'])
    fig_imp.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#F8F9FA', coloraxis_showscale=False, xaxis=dict(showgrid=False), visible=False, yaxis=dict(showgrid=False))
    st.plotly_chart(fig_imp, use_container_width=True, config={'displayModeBar': False})

# ==============================================================================
# TAB 4: ABOUT FBU COMPANY (ИЗОЛИРОВАННЫЙ СТИЛЬ БЕЗ СБОЕВ ДРУГИХ СТРАНИЦ)
# ==============================================================================
with tab4:
    st.write("## 👥 Meet Our Engineering Board")
    st.write("---")
    
    # Полностью изолированный HTML-блок. Карточки светятся ТОЛЬКО здесь.
    # Внутренний код разметки полностью восстановлен и выровнен по середине.
    st.markdown("""
    <style>
        .fbu-card {
            background: rgba(23, 42, 69, 0.4) !important;
            border: 1px solid rgba(0, 112, 192, 0.25) !important;
            border-radius: 16px !important;
            padding: 35px 20px !important;
            box-shadow: 0 8px 25px rgba(0,0,0,0.4) !important;
            text-align: center !important;
            transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
            flex: 1;
        }
        .fbu-card:hover {
            transform: translateY(-8px) scale(1.02) !important;
            border-color: #38EF7D !important;
            box-shadow: 0 0 35px rgba(56, 239, 125, 0.4), 0 15px 40px rgba(0, 0, 0, 0.6) !important;
        }
    </style>
    
    <div style="display: flex; gap: 20px; justify-content: space-between; width: 100%; margin-top: 20px;">
        <div class="fbu-card">
