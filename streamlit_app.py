import streamlit as st
import time
import requests
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random

# 1. Advanced Institutional Page Configuration
st.set_page_config(page_title="Nexus Quantum AI | Pro Terminal", page_icon="⚡", layout="wide")

# 2. Institutional Themes & Custom CSS (Updated for Big Professional Login Card)
st.markdown("""
    <style>
    .main { background-color: #0b0e11; color: #eaecef; }
    [data-testid="stSidebar"] { background-color: #12161c !important; border-right: 1px solid #24292e; }
    
    /* Top Header Bar */
    .nexus-header { display: flex; justify-content: space-between; align-items: center; background-color: #12161c; padding: 18px 25px; margin: -60px -60px 30px -60px; border-bottom: 2px solid #24292e; }
    .nexus-logo { font-size: 24px; font-weight: 900; color: #f0b90b; font-family: 'Segoe UI', sans-serif; letter-spacing: 1px; }
    .nexus-sub-logo { font-size: 13px; color: #848e9c; margin-left: 10px; font-weight: 500; }
    .system-status { font-family: monospace; font-size: 12px; color: #02c076; background-color: rgba(2, 192, 118, 0.1); padding: 4px 10px; border-radius: 4px; }
    
    /* Premium Block Containers */
    .crypto-grid-box { background-color: #161a1e; border: 1px solid #24292e; border-radius: 8px; padding: 25px; margin-bottom: 15px; }
    
    /* Big Bold Professional Login Header & Card */
    .login-title { font-size: 42px; font-weight: 900; color: #f0b90b; font-family: 'Segoe UI', sans-serif; text-align: center; margin-bottom: 5px; letter-spacing: 2px; }
    .login-subtitle { font-size: 16px; color: #848e9c; text-align: center; margin-bottom: 30px; font-weight: 500; }
    .login-card { background: linear-gradient(135deg, #12161c 0%, #1c222a 100%); border: 2px solid #f0b90b; border-radius: 12px; padding: 40px; box-shadow: 0 8px 32px rgba(240, 185, 11, 0.15); max-width: 600px; margin: 0 auto; }
    
    /* Premium Button Customization */
    .stButton>button { width: 100%; background: linear-gradient(135deg, #f0b90b 0%, #f8d347 100%) !important; color: #0b0e11 !important; font-weight: bold; border-radius: 6px; border: none; height: 52px; font-size: 16px; text-transform: uppercase; letter-spacing: 1px; }
    .stButton>button:hover { transform: translateY(-1px); box-shadow: 0 4px 15px rgba(240, 185, 11, 0.4) !important; }
    div[data-testid="stMetricValue"] { font-size: 26px; font-weight: bold; color: #f0b90b !important; }
    
    /* Form Label Styling */
    label[data-testid="stWidgetLabel"] p { font-size: 18px !important; font-weight: bold !important; color: #eaecef !important; }
    </style>
""", unsafe_allow_html=True)

# 3. Secure User Authentication State Management
if "user_db" not in st.session_state:
    st.session_state["user_db"] = {"admin@nexus.com": "admin123"}
if "logged_in_user" not in st.session_state:
    st.session_state["logged_in_user"] = None
if "is_premium" not in st.session_state:
    st.session_state["is_premium"] = False

ADMIN_SECRET_CODE = "NEXUS-PRO-2026"

# Top Executive Header Bar
st.markdown("""
    <div class='nexus-header'>
        <div style='display: flex; align-items: center;'>
            <div class='nexus-logo'>🔶 NEXUS QUANTUM</div>
            <div class='nexus-sub-logo'>High-Frequency Algorithmic Matrix V3.8</div>
        </div>
        <div class='system-status'>● ENGINE ALIVE | FEED: LIVE BINANCE PORTER CONNECTED</div>
    </div>
""", unsafe_allow_html=True)

# --- Big Professional Login & Sign Up Interface ---
if st.session_state["logged_in_user"] is None:
    st.markdown("<div class='login-title'>🔒 ACCESS GATEWAY</div>", unsafe_allow_html=True)
    st.markdown("<div class='login-subtitle'>QUANTUM ALGORITHMIC TRADING TERMINAL V3.8</div>", unsafe_allow_html=True)
    
    # সেন্টার এলাইনড বড় কার্ড ভিউ
    tab1, tab2 = st.tabs(["🔑 REGISTERED SIGN IN", "📝 CREATE MAIN ACCOUNT"])
    
    with tab1:
        st.markdown("<div class='login-card'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color:#f0b90b; text-align:center; margin-top:0;'>SECURE LOGIN</h3>", unsafe_allow_html=True)
        login_email = st.text_input("Enter Gmail Address:", key="login_email")
        login_pass = st.text_input("Enter Password:", type="password", key="login_pass")
        st.write("")
        if st.button("CONNECT TO CORE ENGINE"):
            if login_email in st.session_state["user_db"] and st.session_state["user_db"][login_email] == login_pass:
                st.session_state["logged_in_user"] = login_email
                st.success(f"🎉 Access Granted! Loading Terminal for {login_email}...")
                time.sleep(1)
                st.rerun()
            else:
                st.error("❌ Authentication Failed! Invalid Gmail or Password.")
        st.markdown("</div>", unsafe_allow_html=True)
        
    with tab2:
        st.markdown("<div class='login-card'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color:#f0b90b; text-align:center; margin-top:0;'>LICENSE REGISTRATION</h3>", unsafe_allow_html=True)
        reg_email = st.text_input("Provide Gmail Address:", key="reg_email")
        reg_pass = st.text_input("Create Account Password:", type="password", key="reg_pass")
        reg_confirm = st.text_input("Confirm Account Password:", type="password", key="reg_confirm")
        st.write("")
        if st.button("INITIALIZE TERMINAL LICENSE"):
            if "@" not in reg_email or "." not in reg_email:
                st.error("❌ Invalid Email! Please provide a genuine Gmail account.")
            elif reg_pass != reg_confirm:
                st.error("❌ Synchronize Failed! Passwords do not match.")
            elif reg_email in st.session_state["user_db"]:
                st.error("❌ Identity Conflict! This Gmail is already registered.")
            elif reg_pass == "":
                st.error("❌ Password policy error: Cannot be empty.")
            else:
                st.session_state["user_db"][reg_email] = reg_pass
                st.success("🎉 License Generated! Please switch to the 'SIGN IN' tab to log in.")
        st.markdown("</div>", unsafe_allow_html=True)

# --- After Login: Load Main Algorithmic Bot Dashboard ---
else:
    def get_live_market_data(symbol):
        mocks = {
            'BTCUSDT': {"price": 62894.0, "change": -0.6}, 'ETHUSDT': {"price": 3420.0, "change": 4.1}, 
            'SOLUSDT': {"price": 184.6, "change": 5.8}, 'BNBUSDT': {"price": 585.0, "change": -0.4},
            'XRPUSDT': {"price": 0.62, "change": 1.2}, 'ADAUSDT': {"price": 0.48, "change": -0.5}, 
            'DOTUSDT': {"price": 6.75, "change": 2.3}, 'DOGEUSDT': {"price": 0.14, "change": 3.5}
        }
        return mocks.get(symbol, {"price": 100.0, "change": 0.0})

    symbols = ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'DOTUSDT', 'DOGEUSDT']
    market_data = {sym: get_live_market_data(sym) for sym in symbols}

    # Sidebar Customization
    st.sidebar.markdown("<h3 style='color: #f0b90b; padding-left: 10px; font-weight:800;'>CORE ENGINE</h3>", unsafe_allow_html=True)
    st.sidebar.write(f"👤 **Active Node:** {st.session_state['logged_in_user']}")
    
    st.sidebar.write("---")
    st.sidebar.write("### 👑 Membership Status")
    if st.session_state["is_premium"]:
        st.sidebar.success("👑 PLAN: PREMIUM PRO ACTIVE")
    else:
        st.sidebar.warning("🛡️ PLAN: FREE ACCESS")
        st.sidebar.info("Upgrade to PRO via the Control Hub to unlock trading features.")
        
    st.sidebar.write("---")
    if st.sidebar.button("🚪 TERMINATE SESSION (LOGOUT)"):
        st.session_state["logged_in_user"] = None
        st.session_state["is_premium"] = False
        st.rerun()

    # Main Grid Layout
    st.markdown("<div class='crypto-grid-box'>", unsafe_allow_html=True)
    st.write("### 🪙 Global Liquidity Ticker (Expanded Multi-Coin Scan)")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label="Bitcoin (BTC)", value=f"${market_data['BTCUSDT']['price']:,}", delta=f"{market_data['BTCUSDT']['change']:+.2f}%")
    col2.metric(label="Ethereum (ETH)", value=f"${market_data['ETHUSDT']['price']:,}", delta=f"{market_data['ETHUSDT']['change']:+.2f}%")
    col3.metric(label="Solana (SOL)", value=f"${market_data['SOLUSDT']['price']}", delta=f"{market_data['SOLUSDT']['change']:+.2f}%")
    col4.metric(label="Binance (BNB)", value=f"${market_data['BNBUSDT']['price']}", delta=f"{market_data['BNBUSDT']['change']:+.2f}%")
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.write("---")
    left_layout, right_layout = st.columns([1.6, 1])
    
    with left_layout:
        st.markdown("<div class='crypto-grid-box'>", unsafe_allow_html=True)
        st.write("📈 **HFT Execution Candlestick Analytics**")
        sol_p = market_data['SOLUSDT']['price']
        now = datetime.now()
        dates = [now - timedelta(minutes=x) for x in range(30, 0, -1)]
        opens = [sol_p - random.uniform(-1, 1) for _ in range(30)]
        closes = [o + random.uniform(-1.5, 1.5) for o in opens]
        highs = [max(o, c) + random.uniform(0.1, 0.8) for o, c in zip(opens, closes)]
        lows = [min(o, c) - random.uniform(0.1, 0.8) for o, c in zip(opens, closes)]
        
        fig = go.Figure(data=[go.Candlestick(x=dates, open=opens, high=highs, low=lows, close=closes)])
        fig.update_layout(plot_bgcolor='#161a1e', paper_bgcolor='#0b0e11', xaxis_rangeslider_visible=False, height=300)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with right_layout:
        st.markdown("<div class='crypto-grid-box'>", unsafe_allow_html=True)
        st.write("### 🎛️ Algorithmic Control Hub")
        
        if st.session_state["is_premium"]:
            rr_ratio = st.slider("Set AI Risk-Reward Matrix Target Ratio", 1.0, 5.0, 2.0, step=0.5)
            if st.button("🚀 EXECUTE ALPHA QUANTUM SCAN"):
                st.balloons()
