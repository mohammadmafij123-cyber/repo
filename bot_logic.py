import numpy as np

def check_liquidity_and_order_block(coin, current_price):
    estimated_support_zone = current_price * 0.985 
    estimated_resistance_zone = current_price * 1.015
    if current_price <= (estimated_support_zone * 1.005):
        return True, "Strong Order Block Support (Whale Liquidity)"
    elif current_price >= (estimated_resistance_zone * 0.995):
        return False, "Approaching Heavy Resistance Liquidity"
    else:
        return True, "Normal Trading Range"

def calculate_dynamic_position_size(total_balance, risk_percentage, current_price, stop_loss_price):
    if current_price <= stop_loss_price:
        return 10.0
    allowed_dollar_risk = total_balance * (risk_percentage / 100.0)
    risk_per_unit = current_price - stop_loss_price
    total_trade_investment = (allowed_dollar_risk / risk_per_unit) * current_price
    if total_trade_investment > total_balance:
        return round(total_balance * 0.2, 2)
    return round(total_trade_investment, 2)

def calculate_atr_stop_loss(current_price, atr_value=2.5, multiplier=1.5):
    return round(current_price - (atr_value * multiplier), 2)


# --- Live Binance Wallet Balance Check ---
from binance.client import Client
import streamlit as st

# আপনার আসল বাইনান্স এপিআই তথ্য দুটি এখানে বসান
api_key = "a49Yn6tCuomPjRxVmmLh9DBtyOhjDrpg9X2kEzGJg7sqkrLdC7agBEM4oFYfIROM"
api_secret = "PxI5rtfZ9JFqExa6K25LU4RV3B71hmni9ci8GvWlUVtv5GpHnS1vxzNRONrKBQfy"

try:
    local_client = Client(api_key.strip(), api_secret.strip())
    account_info = local_client.get_account()

    st.sidebar.success("🟢 Binance API 100% Connected Locally!")
    st.sidebar.subheader("💰 Live Wallet Balance")
    has_balance = False
    for asset in account_info['balances']:
        if float(asset['free']) > 0:
            st.sidebar.write(f"**{asset['asset']}:** {asset['free']}")
            has_balance = True
    if not has_balance:
        st.sidebar.info("Your Binance Account Balance is 0.00")
except Exception as e:
    st.sidebar.error(f"🔴 Connection Failed: {e}")
