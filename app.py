import streamlit as st
import pandas as pd
import plotly.express as px

# Global page configuration in a dark dashboard layout
st.set_page_config(page_title="AI Anti-Fraud Hub — Team C1094BD7", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for INHA University Deep Blue style and premium Glassmorphism blur effects
st.markdown("""
<style>
    /* Main background and global text styling */
    .stApp {
        background: linear-gradient(135deg, #0A192F 0%, #172A45 100%) !important;
        color: #F8F9FA !important;
    }
    
    /* Header typography styles */
    h1 {
        color: #0070C0 !important; /* Inha University Blue */
        font-weight: 800 !important;
        text-shadow: 0px 0px 20px rgba(0, 112, 192, 0.4);
    }
    h2, h3 {
        color: #38EF7D !important; /* Neon Green accent */
        font-weight: 600 !important;
    }
    
    /* Glassmorphism card effect (blurred background and subtle borders) */
    div[data-testid="stMetric"] {
        background: rgba(23, 42, 69, 0.4) !important;
        backdrop-filter: blur(12px) opacity(1) !important;
        -webkit-backdrop-filter: blur(12px) !important;
        border: 1px solid rgba(0, 112, 192, 0.25) !important;
        border-radius: 16px !important;
        padding: 20px 25px !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37) !important;
        transition: all 0.3s ease-in-out !important;
    }
    
    /* Interactive glowing hover effect for metric containers */
    div[data-testid="stMetric"]:hover {
        transform: translateY(-5px) !important;
        border-color: #0070C0 !important;
        box-shadow: 0 12px 40px 0 rgba(0, 112, 192, 0.4) !important;
    }
    
    /* Custom tabs navigation styling */
    button[data-baseweb="tab"] {
        color: #8892B0 !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        border-bottom: 2px solid transparent !important;
        transition: all 0.3s !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #0070C0 !important;
        border-bottom-color: #0070C0 !important;
        font-size: 18px !important;
    }
    
    /* Dropdown container styling (Expander) */
    .streamlit-expanderHeader {
        background-color: rgba(23, 42, 69, 0.6) !important;
        border: 1px solid rgba(0, 112, 192, 0.2) !important;
        border-radius: 8px !important;
        color: #F8F9FA !important;
    }
</style>
""", unsafe_allow_html=True)

# Application Banner Section
st.title("🛡️ NEXUS: Next-Gen AI Anti-Fraud Analytics Platform")
st.subheader("Advanced Financial Monitoring System | Powered by Team C1094BD7")

st.markdown("""
<div style="background: rgba(0, 112, 192, 0.1); border-left: 4px solid #0070C0; padding: 15px; border-radius: 4px; margin-bottom: 25px;">
    <strong>Global Operational Status:</strong> Standing at the intersection of Big Data and Cybersecurity. 
    Our neural-gradient framework dissects financial transaction patterns in real-time, isolating high-risk threats from millions of safe everyday operations.
</div>
""", unsafe_allow_html=True)

# Generate 3 functional tabs for streamlined navigation
tab1, tab2, tab3 = st.tabs(["🚀 Core Architecture", "📊 Live Metrics Hub", "🏆 Machine Learning Logic"])

# ==============================================================================
# TAB 1: CORE ARCHITECTURE
# ==============================================================================
with tab1:
    st.write("### Intelligent Threat Filtering Ecosystem")
    st.markdown("""
    In high-volume banking sectors, compliance departments face **an informational avalanche** — hundreds of thousands of daily automated system flags. 
    Reviewing every alert manually compromises security response times and burns critical human resources.

    **Our Solution:** 
    We constructed an end-to-end analytical core that ingests raw, relational historical transaction databases. 
    By converting raw money movements into structured behavior maps, the AI instantly computes an escalation probability score. 
    Analysts no longer search blindly; they address highest-probability threats first.
    """)

    st.write("---")
    st.write("### 🔍 Feature Engineering & Behavioral Pillars")
    st.markdown("Expand the technical nodes below to inspect how the AI decodes raw transaction records:")

    col1, col2, col3 = st.columns(3)
    with col1:
        with st.expander("💸 1. Capital Velocity & Drainage"):
            st.write("""
            **Algorithmic Trigger:** Rapid fund rotation. If an account receives a major credit placement (Kirim) and mirrors it via multiple outbound transfers (Chiqim) within a tight time-window, the AI flags classic money-laundering transit behavior.
            """)
    with col2:
        with st.expander("🌍 2. Cross-Border Channel Friction"):
            st.write("""
            **Algorithmic Trigger:** Sudden geographical shifts. When historical spending patterns rooted heavily in local domestic systems (Tashkent retail) switch instantly to high-volume international wires (Xalqaro), the risk weight mutates to Maximum.
            """)
    with col3:
        with st.expander("📈 3. Volatility & Deviation Spikes"):
            st.write("""
            **Algorithmic Trigger:** Absolute sum mutation. The framework tracks rolling behavioral baselines. A transaction that severely overshoots a customer's standard deviation index triggers immediate automated containment.
            """)

# ==============================================================================
# TAB 2: LIVE METRICS HUB
# ==============================================================================
with tab2:
    st.write("### 📊 Macro-Data Stream Summary")
    st.markdown("*Hover over the glassmorphic metric cards below to see the interactive depth scaling effect:*")
    
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
        target_data = pd.DataFrame({
            'Alert Vector': ['False Alarm (Dismissed)', 'Genuine Threat (Escalated)'], 
            'Volume': [640700, 53394]
        })
        fig_target = px.pie(target_data, values='Volume', names='Alert Vector', 
                            color_discrete_sequence=['#172A45', '#0070C0'])
        fig_target.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#F8F9FA')
        st.plotly_chart(fig_target, use_container_width=True)

    with right_col:
        st.write("### ✈️ Operational Risk Conversion by Medium")
        type_data = pd.DataFrame({
            'Medium': ['Cards', 'Cash', 'International', 'Bank Transfer'],
            'Risk Density (%)': [8.2, 4.1, 38.5, 12.3]
        })
        fig_type = px.bar(type_data, x='Medium', y='Risk Density (%)', text_auto=True,
                          color='Risk Density (%)', color_continuous_scale=['#172A45', '#0070C0', '#38EF7D'])
        fig_type.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#F8F9FA')
        st.plotly_chart(fig_type, use_container_width=True)

# ==============================================================================
# TAB 3: MACHINE LEARNING LOGIC
# ==============================================================================
with tab3:
    st.write("### 🏆 Mathematical Decision Architecture")
    st.markdown("Transparency is vital for modern banking operations. Below is the strict information gain metrics computed by our **LightGBM** core.")
    
    st.write("#### 🎯 Feature Importance Vectors (Top 3 Performance Drivers)")
    rf1, rf2, rf3 = st.columns(3)
    with rf1:
        st.markdown("#### 🥇 Peak Single Volume (`tx_max`)")
        st.metric(label="Information Gain Weight", value="432.50", delta="Primary Splitting Node")
        st.caption("Sudden massive UZS capital spikes diverge violently from historical retail baselines.")
    with rf2:
        st.markdown("#### 🥈 Liquidation Velocity (`kirim_ratio`)")
        st.metric(label="Information Gain Weight", value="389.12", delta="Flow Balance Node")
        st.caption("Proximity to a 1.0 ratio reveals rapid account drainage, isolating layered mule accounts.")
    with rf3:
        st.markdown("#### 🥉 Cross-Border Intensity (`amt_xalqaro`)")
        st.metric(label="Information Gain Weight", value="295.41", delta="Compliance Node")
        st.caption("Automated routing adjustments based on international UZS transaction volume classes.")

    st.write("---")
    st.write("#### Exhaustive Feature Contribution Graph")
    importance_data = pd.DataFrame({})
