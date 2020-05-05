from .constants import *

'''
request = {
    "action": mt5.TRADE_ACTION_PENDING,
    "symbol": symbol,
    "volume": 0.01,
    "type": ORDER_TYPE_BUY_LIMIT,
    "price": price,
    "sl": price - 100 * point,
    "tp": price + 100 * point,
    "deviation": 0,
    "magic": 0,
    "comment": "python script open",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_RETURN,
}


request = {
    "action": mt5.TRADE_ACTION_PENDING,
    "symbol": symbol,
    "volume": 0.01,
    "type": ORDER_TYPE_BUY_LIMIT,
    "price": price,
    "deviation": 0,
    "magic": 0,
    "comment": "python script open",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_RETURN,
}
'''


def send_limit_order(symbol, price, amount):
    request = {
        "action": TRADE_ACTION_PENDING,
        "symbol": symbol,
        "volume": amount,
        "type": ORDER_TYPE_BUY_LIMIT,
        "price": price,
        "deviation": 0,
        "magic": 0,
        "comment": "python script open",
        "type_time": ORDER_TIME_GTC,
        "type_filling": ORDER_FILLING_RETURN,
    }
    print(request)
    return
