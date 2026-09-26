import streamlit as st
import pandas as pd
import plotly.express as px

# Global page configuration
st.set_page_config(page_title="AI Anti-Fraud Hub — Team C1094BD7", layout="wide", initial_sidebar_state="collapsed")

# 4 standard navigation tabs at the very top of the webpage (Heading area)
tab1, tab2, tab3, tab4 = st.tabs(["🚀 Core Architecture", "📊 Live Metrics Hub", "🏆 Machine Learning Logic", "🏢 About FBU"])

# ==============================================================================
# TAB 1: CORE ARCHITECTURE
# ==============================================================================
with tab1:
    st.title("🛡️ NEXUS: Next-Gen AI Anti-Fraud Analytics Platform")
    st.subheader("Advanced Financial Monitoring System | Powered by Team C1094BD7")
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
        fig_type.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#F8F9FA', coloraxis_showscale=False)
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
    fig_imp.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#F8F9FA', coloraxis_showscale=False)
    st.plotly_chart(fig_imp, use_container_width=True, config={'displayModeBar': False})

# ==============================================================================
# TAB 4: ABOUT FBU COMPANY (MONOLITHIC LAYOUT FOR 100% INDENTATION SAFETY)
# ==============================================================================
with tab4:
    # Весь блок вкладки собран в единую HTML-разметку. Это полностью исключает IndentationError в Python.
    st.markdown("""
    <center>
        <!-- Официальный встроенный логотип FBU строго по центру шапки -->
        <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFAAAABQCAYAAACO79l0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAABZ0RVh0Q3JlYXRpb24gVGltZQAwOS8yTy8yNl9678wAAAAidEVYdFNvZnR3YXJlAE1hY3JvbWVkaWEgRmlyZXdvcmtzIE1YIr06OQAAAYZpREFUeNrt20tKg0EUBdDqf9NuwIUwOHAnwSgZg6gZg6gZg6gZg6gZg6gZg6gZg6gZg6gZg6gZg6gZg6gZg6gZg6gZg6gZg6gZg6gZg6gZg6gZg6gZg6gZg6gZg6gZg6gZg6gZg6gZg6gZg6gZg7g78gYv7g7g78gYv7g7g78gYv7g7g78gYv7g7g78gYv7g7g78gYv7g7g78gYv7g7g78gYv7g7g78gYv7g7g78gYv7g7g7DNu8ODuDvyBi/uDuDvyBi/uDuDsM27w4O4O/IGL+4O4O/IGL+4O4OwzbvDg7A78gYv7g7DNu8ODuDvyBi/uDuDvsNfID9v4O7AHzv4OwzbvDg78Acu7g78gYu7A3/g4u7AH7i4O/AHLu4O/IGLuwN/4OLuwB+4uDvwBy7uDvyBi7sDf+Di7sAfuLg78Acu7g78gYu7A3/g4u7AHzv4OwzbvDg7A78gYv7g7DNu8ODuDvsNfID9v4O7AHzv4OwzbvDg78Acu7g78gYu7A3/g4u7AH7i4O/AHLuwP/B87wH8GqLpLgAAAABJRU5ErkJggg==" width="140" style="border-radius:8px; box-shadow:0 4px 15px rgba(0,112,192,0.3); margin-top:10px; margin-bottom:25px;">
    </center>
    
    <h1 style="text-align: center;">🛡️ NEXUS: Next-Gen AI Anti-Fraud Analytics Platform</h1>
    <h3 style="text-align: center; color: #8892B0 !important; font-weight: normal;">Advanced Financial Monitoring System | Powered by Team C1094BD7</h3>
    <br>
    <h2 style="text-align: center; color: #38EF7D !important;">👥 Meet Our Engineering Board</h2>
    <hr style="border-color: rgba(0, 112, 192, 0.2);">
    
    <!-- Стили для красивых заблюренных неоновых карточек участников -->
    <style>
        .custom-card {
            background: rgba(23, 42, 69, 0.45) !important;
            border: 1px solid rgba(0, 112, 192, 0.25) !important;
            border-radius: 12px !important;
            padding: 35px 15px !important;
            box-shadow: 0 8px 25px rgba(0,0,0,0.4) !important;
            text-align: center !important;
            transition: all 0.4s ease-in-out !important;
            flex: 1;
        }
        .custom-card:hover {
            transform: translateY(-8px) scale(1.02) !important;
            border-color: #38EF7D !important;
            box-shadow: 0 0 35px rgba(56, 239, 125, 0.35), 0 15px 40px rgba(0, 0, 0, 0.6) !important;
        }
    </style>
    
    <!-- Строка с тремя карточками, выровненными по центру -->
    <div style="display: flex; gap: 20px; justify-content: space-between; width: 100%; margin-top: 20px;">
        <div class="custom-card">
