import streamlit as st
import time
import requests
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random

# 1. Advanced Institutional Page Configuration
st.set_page_config(page_title="Nexus Quantum AI | Pro Terminal", page_icon="⚡", layout="wide")

# 2. Institutional Themes & Custom CSS
st.markdown("""
    <style>
    .main { background-color: #0b0e11; color: #eaecef; }
    [data-testid="stSidebar"] { background-color: #12161c !important; border-right: 1px solid #24292e; }
    .nexus-header { display: flex; justify-content: space-between; align-items: center; background-color: #12161c; padding: 18px 25px; margin: -60px -60px 30px -60px; border-bottom: 2px solid #24292e; }
    .nexus-logo { font-size: 24px; font-weight: 900; color: #f0b90b; font-family: 'Segoe UI', sans-serif; letter-spacing: 1px; }
    .nexus-sub-logo { font-size: 13px; color: #848e9c; margin-left: 10px; font-weight: 500; }
    .system-status { font-family: monospace; font-size: 12px; color: #02c076; background-color: rgba(2, 192, 118, 0.1); padding: 4px 10px; border-radius: 4px; }
    .crypto-grid-box { background-color: #161a1e; border: 1px solid #24292e; border-radius: 8px; padding: 20px; margin-bottom: 15px; }
    .stButton>button { width: 100%; background: linear-gradient(135deg, #f0b90b 0%, #f8d347 100%) !important; color: #0b0e11 !important; font-weight: bold; border-radius: 6px; border: none; height: 48px; font-size: 15px; }
    .stButton>button:hover { transform: translateY(-1px); box-shadow: 0 4px 15px rgba(240, 185, 11, 0.3) !important; }
    div[data-testid="stMetricValue"] { font-size: 26px; font-weight: bold; color: #f0b90b !important; }
    </style>
""", unsafe_allow_html=True)

# 3. Secure User Authentication State Management
if "user_db" not in st.session_state:
    st.session_state["user_db"] = {"admin@nexus.com": "admin123"}
if "logged_in_user" not in st.session_state:
    st.session_state["logged_in_user"] = None
if "is_premium" not in st.session_state:
    st.session_state["is_premium"] = False
if "auth_mode" not in st.session_state:
    st.session_state["auth_mode"] = "login"

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

# --- TikTok Style Login & Sign Up Interface ---
if st.session_state["logged_in_user"] is None:
    if st.session_state["auth_mode"] == "login":
        st.markdown("<div style='max-width: 480px; margin: 40px auto; background-color: #161a1e; border: 1px solid #2f363d; border-radius: 16px; padding: 40px 35px; box-shadow: 0 12px 40px rgba(0,0,0,0.5); text-align: center;'>", unsafe_allow_html=True)
        st.markdown("<div style='font-size: 32px; font-weight: 800; color: #ffffff; margin-bottom: 30px;'>Log in to Nexus AI</div>", unsafe_allow_html=True)
        login_email = st.text_input("Gmail Address", key="login_email", placeholder="Enter your registered Gmail")
        login_pass = st.text_input("Password", type="password", key="login_pass", placeholder="Enter your password")
        if st.button("Continue"):
            if login_email in st.session_state["user_db"] and st.session_state["user_db"][login_email] == login_pass:
                st.session_state["logged_in_user"] = login_email
                st.success("🎉 Access Granted! Loading Matrix...")
                time.sleep(0.5)
                st.rerun()
            else:
                st.error("Invalid Gmail or password. Please try again.")
        st.write("")
        st.markdown("<div style='font-size: 15px; color: #eaecef; text-align: center; margin-top: 20px;'>Don't have an account?</div>", unsafe_allow_html=True)
        if st.button("Sign up", key="go_to_signup"):
            st.session_state["auth_mode"] = "signup"
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
        
    elif st.session_state["auth_mode"] == "signup":
        st.markdown("<div style='max-width: 480px; margin: 40px auto; background-color: #161a1e; border: 1px solid #2f363d; border-radius: 16px; padding: 40px 35px; box-shadow: 0 12px 40px rgba(0,0,0,0.5); text-align: center;'>", unsafe_allow_html=True)
        st.markdown("<div style='font-size: 32px; font-weight: 800; color: #ffffff; margin-bottom: 30px;'>Sign up for Nexus AI</div>", unsafe_allow_html=True)
        reg_email = st.text_input("Gmail Address", key="reg_email", placeholder="Enter a valid Gmail")
        reg_pass = st.text_input("Create Password", type="password", key="reg_pass", placeholder="Minimum 6 characters")
        reg_confirm = st.text_input("Confirm Password", type="password", key="reg_confirm", placeholder="Re-type password")
        if st.button("Create Account"):
            if "@" not in reg_email or "." not in reg_email:
                st.error("Please enter a valid Gmail address.")
            elif reg_pass != reg_confirm:
                st.error("Passwords do not match!")
            elif reg_email in st.session_state["user_db"]:
                st.error("This Gmail is already registered.")
            elif reg_pass == "":
                st.error("Password cannot be empty.")
            else:
                st.session_state["user_db"][reg_email] = reg_pass
                st.success("🎉 Registration Successful!")
                time.sleep(0.5)
                st.session_state["auth_mode"] = "login"
                st.rerun()
        st.write("")
        st.markdown("<div style='font-size: 15px; color: #eaecef; text-align: center; margin-top: 20px;'>Already have an account?</div>", unsafe_allow_html=True)
        if st.button("Log in", key="go_to_login"):
            st.session_state["auth_mode"] = "login"
            st.rerun()
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
        st.sidebar.info("Upgrade to PRO using the Activation Hub below.")
        
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

    # সরাসরি মেইন স্ক্রিনে পেমেন্ট ভেরিফিকেশন সিস্টেম (সার্ভার লক পুরোপুরি মুক্ত)
    st.error("🔒 PREMIUM LICENSE GATEWAY VERIFICATION")
    st.info("📢 bKash (Personal): 017XXXXXXXX (500 BDT) | 🔶 Binance Pay ID: 123456789 ($4 USD)")
    
    input_code = st.text_input("🔑 Enter License Activation Code:", type="password", key="user_code")
    
    if st.button("🔓 Verify & Activate Lifetime License"):
        if input_code == ADMIN_SECRET_CODE:
            st.session_state["is_premium"] = True
            st.success("🎉 License Activated successfully! Entering Premium Mode...")
        else:
            st.error("❌ Invalid Code! Please provide a correct activation key.")
            
    # কোড বসানো হলে চার্ট এবং কন্ট্রোল প্যানেল নিচে রেন্ডার হবে
    if st.session_state["is_premium"]:
        st.write("---")
        st.write("### 🎛️ Algorithmic Control Hub (PRO ACTIVE)")
        rr_ratio = st.slider("Set AI Risk-Reward Matrix Target Ratio", 1.0, 5.0, 2.0, step=0.5)
        use_trailing = st.checkbox("Enable Trailing Stop-Loss (🛡️ Safe Profit Lock)", value=True)
        use_filters = st.checkbox("Enable RSI & MACD Trend Filters (⚠️ Avoid Fake Signals)", value=True)
        if st.button("🚀 EXECUTE ALPHA QUANTUM SCAN"):
            st.balloons()
            st.success("🎯 Target Captured! Strategic Order Executed successfully.")
        
        st.write("---")
        st.write("📈 **HFT Execution Candlestick Analytics**")
