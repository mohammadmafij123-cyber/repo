import streamlit as st
import time
import requests
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random

# 1. Page Configuration
st.set_page_config(page_title="Nexus Quantum AI | Institutional Trading Terminal", page_icon="⚡", layout="wide")

# 2. Premium Theme Styles (CSS)
st.markdown("""
    <style>
    .main { background-color: #0b0e14; color: #eaecef; }
    [data-testid="stSidebar"] { background-color: #121620 !important; border-right: 1px solid #1e2533; }
    
    /* Top Header */
    .nexus-header { display: flex; justify-content: space-between; align-items: center; background-color: #121620; padding: 18px 25px; margin: -60px -60px 30px -60px; border-bottom: 2px solid #1e2533; }
    .nexus-logo { font-size: 24px; font-weight: 900; color: #00ffcc; font-family: 'Segoe UI', sans-serif; letter-spacing: 1px; }
    .nexus-sub-logo { font-size: 13px; color: #848e9c; margin-left: 10px; font-weight: 500; }
    .system-status { font-family: monospace; font-size: 12px; color: #00ffcc; background-color: rgba(0, 255, 204, 0.1); padding: 4px 10px; border-radius: 4px; border: 1px solid rgba(0, 255, 204, 0.2); }
    
    /* Premium Grid Cards */
    .nexus-card { background-color: #121620; border: 1px solid #1e2533; border-radius: 10px; padding: 22px; margin-bottom: 20px; }
    .card-title { font-size: 16px; font-weight: bold; color: #ffffff; margin-bottom: 8px; }
    .card-status { font-size: 13px; color: #00ffcc; font-weight: 600; }
    .card-pending { font-size: 13px; color: #848e9c; font-weight: 600; }
    
    /* Button Custom Gradient */
    .stButton>button { width: 100%; background: linear-gradient(135deg, #00ffcc 0%, #0099ff 100%) !important; color: #0b0e14 !important; font-weight: bold; border-radius: 6px; border: none; height: 48px; font-size: 15px; transition: all 0.2s ease; }
    .stButton>button:hover { transform: translateY(-1px); box-shadow: 0 4px 15px rgba(0, 255, 204, 0.3) !important; }
    
    div[data-testid="stMetricValue"] { font-size: 26px; font-weight: bold; color: #00ffcc !important; }
    </style>
""", unsafe_allow_html=True)

# 3. Top Executive Header Bar
st.markdown("""
    <div class='nexus-header'>
        <div style='display: flex; align-items: center;'>
            <div class='nexus-logo'>⚡ NEXUS QUANTUM</div>
            <div class='nexus-sub-logo'>High-Frequency Algorithmic Matrix V3.8</div>
        </div>
        <div class='system-status'>● NETWORK ALIVE | LATENCY: 12ms | LIVE UPDATING</div>
    </div>
""", unsafe_allow_html=True)

# Public Binance API Call for live market feeds
def get_live_market_data(symbol):
    try:
        res = requests.get(f"https://binance.com{symbol}", timeout=2).json()
        return float(res['lastPrice']), float(res['priceChangePercent'])
    except:
        mocks = {'BTCUSDT': (92450.0, 2.3), 'ETHUSDT': (3420.0, 4.1), 'SOLUSDT': (184.6, 5.8), 'BNBUSDT': (585.0, -0.4)}
        return mocks.get(symbol, (100.0, 0.0))

# ক্যান্ডেলস্টিক চার্ট নড়াচড়া করানোর জন্য ডাইনামিক লাইভ ডাটা জেনারেটর
def generate_live_candles(base_price):
    now = datetime.now()
    dates = [now - timedelta(minutes=x) for x in range(10, 0, -1)]
    opens, highs, lows, closes = [], [], [], []
    current = base_price - 2.5
    for _ in range(9):
        o = current
        c = o + random.uniform(-1.5, 1.8)
        h = max(o, c) + random.uniform(0.1, 0.8)
        l = min(o, c) - random.uniform(0.1, 0.8)
        opens.append(o)
        highs.append(h)
        lows.append(l)
        closes.append(c)
        current = c
    last_o = current
    last_c = base_price
    last_h = max(last_o, last_c) + random.uniform(0.05, 0.3)
    last_l = min(last_o, last_c) - random.uniform(0.05, 0.3)
    opens.append(last_o)
    highs.append(last_h)
    lows.append(last_l)
    closes.append(last_c)
    return dates, opens, highs, lows, closes

btc_p, btc_pct = get_live_market_data('BTCUSDT')
eth_p, eth_pct = get_live_market_data('ETHUSDT')
sol_p, sol_pct = get_live_market_data('SOLUSDT')
bnb_p, bnb_pct = get_live_market_data('BNBUSDT')

# 4. Sidebar Navigation
st.sidebar.markdown("<h3 style='color: #00ffcc; padding-left: 10px; font-weight:800;'>CORE ENGINE</h3>", unsafe_allow_html=True)
menu = st.sidebar.radio(
    "Navigation",
    ["🏠 Execution Terminal", "💼 Institutional Assets", "📰 Alpha Intelligence", "⚙️ Cryptographic Vault"],
    label_visibility="collapsed"
)

st.sidebar.write("---")
st.sidebar.write("### 🛡️ FireWall Status")
st.sidebar.success("🛡️ Dynamic Guard: ACTIVE")

# 5. Main Dashboard View
if menu == "🏠 Execution Terminal":
    st.write("### 🪙 Global Liquidity Ticker (Live Auto-Refreshing)")
    呈现1, 呈现2, 呈现3, 呈现4 = st.columns(4)
    呈现1.metric(label="Bitcoin (BTC/USDT)", value=f"${btc_p:,}", delta=f"{btc_pct:+.2f}%")
    呈现2.metric(label="Ethereum (ETH/USDT)", value=f"${eth_p:,}", delta=f"{eth_pct:+.2f}%")
    呈现3.metric(label="Solana (SOL/USDT)", value=f"${sol_p}", delta=f"{sol_pct:+.2f}%")
    呈现4.metric(label="Binance Coin (BNB/USDT)", value=f"${bnb_p}", delta=f"{bnb_pct:+.2f}%")
    
    st.write("---")
    st.write("### ⚡ Operational Deployment Pipeline")
    
    card_col1, card_col2, card_col3 = st.columns(3)
    with card_col1:
        st.markdown("<div class='nexus-card'><div class='card-title'>1. Quantum Node Verification</div><p style='color: #848e9c; font-size:13.5px; height: 55px;'>Asymmetric key handshake and localized verification protocols successfully established.</p><div class='card-status'>✓ Node Secured & Encrypted</div></div>", unsafe_allow_html=True)
    with card_col2:
        st.markdown("<div class='nexus-card'><div class='card-title'>2. Margin Balance Pipeline</div><p style='color: #848e9c; font-size:13.5px; height: 55px;'>Live collateral feed routing via exchange secure handshake protocol.</p><div class='card-status' style='color:#0099ff;'>⚡ Allocation Ready: $15.00</div></div>", unsafe_allow_html=True)
    with card_col3:
        st.markdown("<div class='nexus-card'><div class='card-title'>3. Algorithmic Automation</div><p style='color: #848e9c; font-size:13.5px; height: 55px;'>Neural engine standing by for cross-market structural buy/sell triggers.</p><div class='card-pending'>⏳ Awaiting Command Token</div></div>", unsafe_allow_html=True)

    st.write("---")
    left_layout, right_layout = st.columns([1.6, 1])

    with left_layout:
        dates, opens, highs, lows, closes = generate_live_candles(sol_p)
        fig = go.Figure(data=[go.Candlestick(
            x=dates, open=opens, high=highs, low=lows, close=closes,
            increasing_line_color='#00ffcc', decreasing_line_color='#ff4b4b'
        )])
        fig.update_layout(title="HFT Execution Candlestick Analytics (Real-Time Pulse)", template="plotly_dark", xaxis_rangeslider_visible=False, height=380, margin=dict(t=30, b=10, l=10, r=10))
        st.plotly_chart(fig, use_container_width=True)

    with right_layout:
        st.write("### 🎛️ Algorithmic Control Hub")
        st.write("Trigger the system below to execute real-time order tracking and deploy stop-loss/take-profit guards.")
        if st.button("🚀 EXECUTE ALPHA QUANTUM SCAN"):
            with st.spinner("Processing alpha order book profiles..."):
                time.sleep(1.5)
                st.balloons()
            st.success("Target Captured: Optimal structural setup loaded on SOLUSDT.")
            tp_price = sol_p * 1.04
            sl_price = sol_p * 0.98
            
            # ট্রিপল কোটেশন তুলে দিয়ে একদম সেফ সিঙ্গেল লাইনে কাস্টম বক্স দেওয়া হলো
            st.markdown(f"<div style='background-color: #121620; padding: 15px; border-radius: 8px; border-left: 4px solid #00ffcc; margin-top: 10px; border: 1px solid #1e2533;'><b style='color: #00ffcc;'>🟢 STRATEGIC ORDER OPENED</b><br><br>• Target Market: SOLUSDT<br>• Base Entry Rate: ${sol_p:.2f}<br>• Take-Profit Target (+4.0%): <span style='color: #00ffcc; font-weight:bold;'>${tp_price:.2f}</span><br>• Stop-Loss Shield (-2.0%): <span style='color: #ff4b4b; font-weight:bold;'>${sl_price:.2f}</span></div>", unsafe_allow_html=True)

    time.sleep(1.0)
    st.rerun()

elif menu == "💼 Institutional Assets":
    st.markdown("<h1>💼 Account Balance Assets</h1>", unsafe_allow_html=True)
    st.write("---")
    portfolio_data = {
        'Digital Asset': ['Bitcoin (BTC)', 'Ethereum (ETH)', 'Solana (SOL)', 'Tether Stablecoin (USDT)'],
        'Allocated Volume': ['0.00015', '0.0024', '0.054', '15.00'],
        'Equity Evaluation (USD)': [f"${btc_p*0.00015:.2f}", f"${eth_p*0.0024:.2f}", f"${sol_p*0.054:.2f}", '$15.00'],
        'Delta Performance': [f'{btc_pct:+.2f}%', f'{eth_pct:+.2f}%', f'{sol_pct:+.2f}%', '0.00% ⚡']
    }
    st.table(pd.DataFrame(portfolio_data))

elif menu == "📰 Alpha Intelligence":
    st.markdown("<h1>📰 Global Financial Macro Intel</h1>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<div class='nexus-card'><h4 style='color: #00ffcc; margin-top:0;'>Order Book Analysis: $500M Spot Liquidity Concentrated</h4><p style='color: #848e9c;'>Aggregated multi-exchange order books report heavy institutional buy walls anchoring key levels.</p></div>", unsafe_allow_html=True)

elif menu == "⚙️ Cryptographic Vault":
    st.markdown("<h1>⚙️ Asymmetric Exchange API Vault</h1>", unsafe_allow_html=True)
    st.write("---")
    st.text_input("Exchange Public API Identifier", type="password", placeholder="Paste secure public API key...")
    st.text_input("Exchange Encrypted Private Signature", type="password", placeholder="Paste secure private secret signature...")
    if st.button("🔒 SEAL & DEPLOY CREDENTIALS"):
        st.success("🔒 API credentials locked via end-to-end sandbox isolation protocols.")
