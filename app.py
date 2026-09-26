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
    st.title("🛡 NEXUS: Next-Gen AI Anti-Fraud Analytics Platform")
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
    fig_imp.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#F8F9FA', coloraxis_showscale=False, xaxis=dict(showgrid=False, visible=False), yaxis=dict(showgrid=False))
    st.plotly_chart(fig_imp, use_container_width=True, config={'displayModeBar': False})


# ==============================================================================
# TAB 4: ABOUT FBU COMPANY (CENTERED & EXPANDED PROFILE LAYOUT)
# ==============================================================================
with tab4:
    st.title("🛡 NEXUS: Next-Gen AI Anti-Fraud Analytics Platform")
    st.subheader("Advanced Financial Monitoring System | Powered by Team C1094BD7")
    st.write("## 👥 Meet Our Engineering Board")
    st.write("---")
    
    p1, p2, p3 = st.columns(3)
    
    # Pre-loading localized data representations to prevent compilation breakage
    avatar_html = "<center><br><div style='font-size:75px; color:#8892B0; margin-bottom:10px;'>👤</div>"
    
    with p1:
        with st.container(border=True):
            st.markdown(avatar_html + "<h2 style='margin:0; font-size:28px; color:#FFFFFF;'>Nurillayev Ulug'bek</h2><p style='color:#38EF7D; font-weight:bold; font-size:15px; margin-top:8px; margin-bottom:8px;'>Captain & Lead Systems Director, FBU</p><p style='color:#8892B0; font-size:14px; margin:0;'>🎓 Student at Inha University in Tashkent (IUT)</p><br><p style='margin-top:10px; margin-bottom:5px;'>📞 <b>Contact:</b> +998774147727</p><p style='margin:0;'>✈️ <b>Telegram:</b> @nurullaeev</p><br></center>", unsafe_allow_html=True)

    with p2:
        with st.container(border=True):
            st.markdown(avatar_html + "<h2 style='margin:0; font-size:28px; color:#FFFFFF;'>Nabijonov Firdavs</h2><p style='color:#38EF7D; font-weight:bold; font-size:15px; margin-top:8px; margin-bottom:8px;'>Senior Vibe Engineer & Full-Stack</p><p style='color:#8892B0; font-size:14px; margin:0;'>🎓 Student at Inha University in Tashkent (IUT)</p><br><p style='margin-top:10px; margin-bottom:5px;'>📞 <b>Contact:</b> +998902535318</p><p style='margin:0;'>✈️ <b>Telegram:</b> @nabijanov111</p><br></center>", unsafe_allow_html=True)

    with p3:
        with st.container(border=True):
            st.markdown(avatar_html + "<h2 style='margin:0; font-size:28px; color:#FFFFFF;'>Soxibov Baxtiyorjon</h2><p style='color:#38EF7D; font-weight:bold; font-size:15px; margin-top:8px; margin-bottom:8px;'>Strategic Innovation Head</p><p style='color:#8892B0; font-size:14px; margin:0;'>🎓 Student at Inha University in Tashkent (IUT)</p><br><p style='margin-top:10px; margin-bottom:5px;'>📞 <b>Contact:</b> +998507797229</p><p style='margin:0;'>✈️ <b>Telegram:</b> @sbyxha</p><br></center>", unsafe_allow_html=True)

st.write("---")
st.markdown("<div style='text-align: center; color: #8892B0; font-size: 13px;'>🏢 FBU CORPORATION &nbsp;|&nbsp; 🏢 INHA UNIVERSITY IN TASHKENT (IUT)</div>", unsafe_allow_html=True)
