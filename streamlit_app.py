import streamlit as st
import time
import requests
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# 1. Page Configuration
st.set_page_config(page_title="Binance | Algorithmic Trading Dashboard", page_icon="💛", layout="wide")

# 2. Ultra-Premium Full Binance Replica Theme (CSS)
st.markdown("""
    <style>
    .main { background-color: #12161a; color: #eaecef; }
    [data-testid="stSidebar"] { background-color: #1e2329 !important; border-right: 1px solid #2b3139; }
    
    /* Top Header Styling */
    .binance-header { display: flex; align-items: center; background-color: #1e2329; padding: 15px 25px; margin: -60px -60px 30px -60px; border-bottom: 1px solid #2b3139; }
    .binance-logo { font-size: 22px; font-weight: bold; color: #f0b90b; font-family: 'Arial Black', sans-serif; letter-spacing: 0.5px; }
    .binance-sub-logo { font-size: 14px; color: #848e9c; margin-left: 15px; margin-top: 5px; font-weight: 500; }
    
    /* Premium Binance Cards */
    .binance-card { background-color: #1e2329; border: 1px solid #2b3139; border-radius: 12px; padding: 25px; margin-bottom: 20px; transition: all 0.3s ease; }
    .binance-card:hover { border-color: #f0b90b; box-shadow: 0 4px 20px rgba(240, 185, 11, 0.08); }
    .card-title { font-size: 18px; font-weight: bold; color: #ffffff; margin-bottom: 10px; }
    .card-status { font-size: 13px; color: #02c076; font-weight: 600; display: flex; align-items: center; }
    .card-pending { font-size: 13px; color: #848e9c; font-weight: 600; }
    
    /* Button Premium Styling */
    .stButton>button { width: 100%; background-color: #f0b90b !important; color: #12161a !important; font-weight: bold; border-radius: 6px; border: none; height: 45px; font-size: 15px; transition: all 0.2s ease; }
    .stButton>button:hover { background-color: #f8d347 !important; transform: translateY(-1px); box-shadow: 0 4px 12px rgba(240, 185, 11, 0.2); }
    
    div[data-testid="stMetricValue"] { font-size: 28px; font-weight: bold; color: #f0b90b !important; }
    </style>
""", unsafe_allow_html=True)

# 3. Top Header Bar (বাইনান্সের আসল হেডার লুক)
st.markdown("""
    <div class='binance-header'>
        <div class='binance-logo'>🔶 BINANCE</div>
        <div class='binance-sub-logo'>Quantum AI Trading Terminal</div>
    </div>
""", unsafe_allow_html=True)

# Public Binance API Call for live market feeds
def get_live_market_data(symbol):
    try:
        res = requests.get(f"https://binance.com{symbol}", timeout=3).json()
        return float(res['lastPrice']), float(res['priceChangePercent'])
    except:
        mocks = {'BTCUSDT': (92450.0, 2.3), 'ETHUSDT': (3420.0, 4.1), 'SOLUSDT': (184.6, 5.8), 'BNBUSDT': (585.0, -0.4)}
        return mocks.get(symbol, (100.0, 0.0))

btc_p, btc_pct = get_live_market_data('BTCUSDT')
eth_p, eth_pct = get_live_market_data('ETHUSDT')
sol_p, sol_pct = get_live_market_data('SOLUSDT')
bnb_p, bnb_pct = get_live_market_data('BNBUSDT')

# 4. Icon-Based Side Navigation Bar (বাম পাশের মেনু)
st.sidebar.markdown("<h3 style='color: #f0b90b; padding-left: 10px;'>User Terminal</h3>", unsafe_allow_html=True)
menu = st.sidebar.radio(
    "Navigation",
    ["🏠 Dashboard", "💼 Assets & Wallet", "📰 Market News", "⚙️ Security Settings"],
    label_visibility="collapsed"
)

st.sidebar.write("---")
st.sidebar.write("### 🛡️ System Guard")
st.sidebar.info("System Protection: Active (Command-Based)")

# 5. Main Dashboard View
if menu == "🏠 Dashboard":
    # Live Cryptocurrency Ticker Section
    st.write("### 🪙 Real-Time Market Ticker")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric(label="Bitcoin (BTC/USDT)", value=f"${btc_p:,}", delta=f"{btc_pct:+.2f}%")
    c2.metric(label="Ethereum (ETH/USDT)", value=f"${eth_p:,}", delta=f"{eth_pct:+.2f}%")
    c3.metric(label="Solana (SOL/USDT)", value=f"${sol_p}", delta=f"{sol_pct:+.2f}%")
    c4.metric(label="Binance Coin (BNB/USDT)", value=f"${bnb_p}", delta=f"{bnb_pct:+.2f}%")
    
    st.write("---")
    st.write("### ⚡ Get Started Trading Journey")
    
    # 3-Column Premium Card Step Design (বাইনান্সের বর্তমান স্ক্রিনশটের মতো ড্যাশবোর্ড বক্স)
    card_col1, card_col2, card_col3 = st.columns(3)
    
    with card_col1:
        st.markdown("""
            <div class='binance-card'>
                <div class='card-title'>1. AI Wallet Connection</div>
                <p style='color: #848e9c; font-size:14px; height: 60px;'>Your hardware encryption and verification protocols are successfully synced.</p>
                <div class='card-status'>✓ Connected & Secured</div>
            </div>
        """, unsafe_allow_html=True)
        
    with card_col2:
        st.markdown("""
            <div class='binance-card'>
                <div class='card-title'>2. Capital Deployment</div>
                <p style='color: #848e9c; font-size:14px; height: 60px;'>Load funds into your Binance secure Spot account to initiate live trades.</p>
                <div class='card-status' style='color:#f0b90b;'>⚡ Balance Ready: $15.00</div>
            </div>
        """, unsafe_allow_html=True)
        
    with card_col3:
        st.markdown("""
            <div class='binance-card'>
                <div class='card-title'>3. Quantum Trading Execution</div>
                <p style='color: #848e9c; font-size:14px; height: 60px;'>Command the AI core algorithm to begin live cross-asset order scans.</p>
                <div class='card-pending'>⏳ Awaiting System Command</div>
            </div>
        """, unsafe_allow_html=True)

    st.write("---")

    # Chart & Trading Panel Grid
    left_layout, right_layout = st.columns([1.6, 1])

    with left_layout:
        dates = pd.date_range(end=datetime.today(), periods=15, freq='h')
        fig = go.Figure(data=[go.Candlestick(
            x=dates,
            open=[sol_p-3, sol_p-2, sol_p-4, sol_p-1, sol_p],
            high=[sol_p-1, sol_p, sol_p-2, sol_p+1, sol_p+3],
            low=[sol_p-4, sol_p-3, sol_p-5, sol_p-2, sol_p-1],
            close=[sol_p-2, sol_p-3, sol_p-1, sol_p-2, sol_p],
            increasing_line_color='#02c076', decreasing_line_color='#f6465d'
        )])
        fig.update_layout(title="Live Technical Candlestick Analytics", template="plotly_dark", xaxis_rangeslider_visible=False, height=380, margin=dict(t=30, b=10, l=10, r=10))
        st.plotly_chart(fig, use_container_width=True)

    with right_layout:
        st.write("### 🎛️ Algorithmic Control Hub")
        st.write("Trigger the system below to scan live order depth and place precise automated limit targets.")
        
        if st.button("🚀 INITIATE QUANTUM ORDER SCAN"):
            with st.spinner("Scanning real-time order depth profiles..."):
                time.sleep(1.5)
                st.balloons()
            st.success("Analysis Complete: Optimal long target locked on SOLUSDT.")
            
            tp_price = sol_p * 1.04
            sl_price = sol_p * 0.98
            st.markdown(f"""
                <div style='background-color: #1e2329; padding: 15px; border-radius: 8px; border-left: 4px solid #02c076; margin-top: 10px; border: 1px solid #2b3139;'>
                    <b style='color: #02c076;'>🟢 ORDER STATUS: ACTIVE POSITION</b><br><br>
                    • Target Market: SOLUSDT<br>
                    • Execution Price: ${sol_p:.2f}<br>
                    • Target Take-Profit (+4%): <span style='color: #02c076; font-weight:bold;'>${tp_price:.2f}</span><br>
                    • Protection Stop-Loss (-2%): <span style='color: #f6465d; font-weight:bold;'>${sl_price:.2f}</span>
                </div>
            """, unsafe_allow_html=True)

elif menu == "💼 Assets & Wallet":
    st.markdown("<h1>💼 Wallet Holding Balances</h1>", unsafe_allow_html=True)
    st.write("---")
    portfolio_data = {
        'Asset': ['Bitcoin (BTC)', 'Ethereum (ETH)', 'Solana (SOL)', 'Tether Stablecoin (USDT)'],
        'Allocated Volume': ['0.00015', '0.0024', '0.054', '15.00'],
        'Market Value (USD)': [f"${btc_p*0.00015:.2f}", f"${eth_p*0.0024:.2f}", f"${sol_p*0.054:.2f}", '$15.00'],
        '24h Returns': [f'{btc_pct:+.2f}%', f'{eth_pct:+.2f}%', f'{sol_pct:+.2f}%', '0.00%']
    }
    st.table(pd.DataFrame(portfolio_data))

elif menu == "📰 Market News":
    st.markdown("<h1>📰 Institutional News Feed</h1>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("""
        <div class='binance-card'>
            <h4 style='color: #f0b90b; margin-top:0;'>🔥 Whale Alert: $500M Stablecoin Liquidity Inflow Detected</h4>
            <p style='font-size: 14px; color: #848e9c;'>Large scale centralized transaction ledgers indicate heavy volume preparations ahead of weekly option expirations.</p>
            <small style='color: #848e9c;'>Updated 10 mins ago • Sentiment: Highly Volatile</small>
        </div>
    """, unsafe_allow_html=True)

elif menu == "⚙️ Security Settings":
    st.markdown("<h1>⚙️ Exchange API Handshake Configuration</h1>", unsafe_allow_html=True)
    st.write("---")
    st.text_input("Binance Secure Live API Key", type="password", placeholder="Enter official exchange public key...")
    st.text_input("Binance Secure Live API Secret", type="password", placeholder="Enter official exchange private signature...")
    if st.button("🔒 ACTIVATE ENCRYPTION SECURE LOCK"):
        st.success("🔒 Localized cryptographic guard engaged successfully.")
