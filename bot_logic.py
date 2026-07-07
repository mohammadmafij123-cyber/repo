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
