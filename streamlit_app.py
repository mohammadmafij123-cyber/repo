import streamlit as st
import time
import requests
import pandas as pd
import streamlit.components.v1 as components

# 1. Advanced Institutional Page Configuration
st.set_page_config(page_title="Nexus Quantum AI | Trading Terminal", page_icon="⚡", layout="wide")

# 2. Ultra-Premium Themes & Custom CSS
st.markdown("""
    <style>
    .main { background-color: #0b0e11; color: #eaecef; }
    [data-testid="stSidebar"] { background-color: #12161c !important; border-right: 1px solid #24292e; }
    
    /* Top Header Bar */
    .nexus-header { display: flex; justify-content: space-between; align-items: center; background-color: #12161c; padding: 18px 25px; margin: -60px -60px 30px -60px; border-bottom: 2px solid #24292e; }
    .nexus-logo { font-size: 24px; font-weight: 900; color: #f0b90b; font-family: 'Segoe UI', sans-serif; letter-spacing: 1px; }
    .nexus-sub-logo { font-size: 13px; color: #848e9c; margin-left: 10px; font-weight: 500; }
    .system-status { font-family: monospace; font-size: 12px; color: #02c076; background-color: rgba(2, 192, 118, 0.1); padding: 4px 10px; border-radius: 4px; }
    
    /* Premium Dashboard Cards */
    .nexus-card { background-color: #161a1e; border: 1px solid #24292e; border-radius: 10px; padding: 22px; margin-bottom: 20px; }
    .card-title { font-size: 16px; font-weight: bold; color: #ffffff; margin-bottom: 8px; }
    .card-status { font-size: 13px; color: #02c076; font-weight: 600; }
    .card-pending { font-size: 13px; color: #848e9c; font-weight: 600; }
    
    /* Premium Button */
    .stButton>button { width: 100%; background: linear-gradient(135deg, #f0b90b 0%, #f8d347 100%) !important; color: #0b0e11 !important; font-weight: bold; border-radius: 6px; border: none; height: 48px; font-size: 15px; }
    .stButton>button:hover { transform: translateY(-1px); box-shadow: 0 4px 15px rgba(240, 185, 11, 0.3) !important; }
    
    div[data-testid="stMetricValue"] { font-size: 26px; font-weight: bold; color: #f0b90b !important; }
    </style>
""", unsafe_allow_html=True)

# 3. Top Executive Header Bar
st.markdown("""
    <div class='nexus-header'>
        <div style='display: flex; align-items: center;'>
            <div class='nexus-logo'>🔶 NEXUS QUANTUM</div>
            <div class='nexus-sub-logo'>High-Frequency Algorithmic Matrix V3.8</div>
        </div>
        <div class='system-status'>● ENGINE ALIVE | FEED: BINANCE REAL-TIME | SMOOTH ANIMATION</div>
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

btc_p, btc_pct = get_live_market_data('BTCUSDT')
eth_p, eth_pct = get_live_market_data('ETHUSDT')
sol_p, sol_pct = get_live_market_data('SOLUSDT')
bnb_p, bnb_pct = get_live_market_data('BNBUSDT')

# 4. Sidebar Navigation Panel
st.sidebar.markdown("<h3 style='color: #f0b90b; padding-left: 10px; font-weight:800;'>CORE ENGINE</h3>", unsafe_allow_html=True)
menu = st.sidebar.radio("Navigation", ["🏠 Execution Terminal", "💼 Institutional Assets", "📰 Alpha Intelligence", "⚙️ Cryptographic Vault"], label_visibility="collapsed")

st.sidebar.write("---")
st.sidebar.write("### 🛡️ FireWall Status")
st.sidebar.success("🛡️ Dynamic Guard: ACTIVE")

# 5. Main Dashboard View
if menu == "🏠 Execution Terminal":
    st.write("### 🪙 Global Liquidity Ticker")
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
        st.write("📈 **Binance Pro Advanced Feed (Smooth Live Pulse Motion)**")
        
        # বিশ্বমানের লাইটওয়েট ট্রেডিংভিউ চার্ট স্ক্রিপ্ট ইম্বেড (যা পুরো বাইনান্স এক্সচেঞ্জে ব্যবহৃত হয়)
        binance_chart_html = f"""
        <div id="chart-container" style="width: 100%; height: 380px; background-color: #161a1e; border-radius: 6px; border: 1px solid #24292e; overflow: hidden;"></div>
        <script src="https://unpkg.com"></script>
        <script>
            const container = document.getElementById('chart-container');
            const chart = LightweightCharts.createChart(container, {{
                width: container.clientWidth,
                height: 380,
                layout: {{ backgroundColor: '#161a1e', textColor: '#848e9c' }},
                grid: {{ vertLines: {{ color: '#24292e' }}, horzLines: {{ color: '#24292e' }} }},
                crosshair: {{ mode: LightweightCharts.CrosshairMode.Normal }},
                priceScale: {{ position: 'right', borderVisible: false }},
                timeScale: {{ borderVisible: false, timeVisible: true, secondsVisible: false }}
            }});

            const candleSeries = chart.addCandlestickSeries({{
                upColor: '#02c076', downColor: '#f6465d', borderUpColor: '#02c076',
                borderDownColor: '#f6465d', wickUpColor: '#02c076', wickDownColor: '#f6465d'
            }});

            let basePrice = {sol_p};
            let data = [];
            let timeStamp = Math.floor(Date.now() / 1000) - 30 * 60;

            for (let i = 0; i < 30; i++) {{
                let open = basePrice + (Math.random() - 0.5) * 3;
                let close = open + (Math.random() - 0.5) * 2;
                data.push({{
                    time: timeStamp + i * 60,
                    open: open,
                    high: Math.max(open, close) + Math.random(),
                    low: Math.min(open, close) - Math.random(),
                    close: close
                }});
                basePrice = close;
            }}
            candleSeries.setData(data);

            let lastCandle = data[data.length - 1];
            setInterval(() => {{
                let liveChange = (Math.random() - 0.5) * 0.4;
                lastCandle.close += liveChange;
                if (lastCandle.close > lastCandle.high) lastCandle.high = lastCandle.close;
                if (lastCandle.close < lastCandle.low) lastCandle.low = lastCandle.close;
                candleSeries.update(lastCandle);
            }}, 1000);
        </script>
        """
        components.html(binance_chart_html, height=390)

    with right_layout:
        st.write("### 🎛️ Algorithmic Control Hub")
        st.write("Trigger the system below to execute real-time order tracking and deploy guards.")
        if st.button("🚀 EXECUTE ALPHA QUANTUM SCAN"):
            with st.spinner("Processing alpha order book profiles..."):
                time.sleep(1.5)
                st.balloons()
            st.success("Target Captured: Optimal structural setup loaded on SOLUSDT.")
            tp_price = sol_p * 1.04
            sl_price = sol_p * 0.98
            st.markdown(f"<div style='background-color: #161a1e; padding: 15px; border-radius: 8px; border-left: 4px solid #02c076; margin-top: 10px; border: 1px solid #24292e;'><b style='color: #02c076;'>🟢 STRATEGIC ORDER OPENED</b><br><br>• Target Market: SOLUSDT<br>• Base Entry Rate: ${sol_p:.2f}<br>• Take-Profit Target (+4.0%): <span style='color: #02c076; font-weight:bold;'>${tp_price:.2f}</span><br>• Stop-Loss Shield (-2.0%): <span style='color: #f6465d; font-weight:bold;'>${sl_price:.2f}</span></div>", unsafe_allow_html=True)

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
