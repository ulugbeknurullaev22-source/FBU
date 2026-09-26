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
