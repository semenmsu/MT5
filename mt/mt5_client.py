from datetime import datetime
import time
import MetaTrader5 as mt5
from .logger import logger
from .constants import *


class MT5Client:
    def __init__(self):
        if not mt5.initialize():
            print("initialize() failed")
            mt5.shutdown()
            exit(1)
        else:
            print("initialize ok")

    def ticker(self, symbol):
        ticker = mt5.symbol_info_tick(symbol)
        logger.debug(ticker, extra={'type': "update"})
        return (ticker.bid, ticker.ask, ticker.time_msc)

    def send_limit_order(self, symbol, price, amount):
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

        logger.debug(request, extra={'type': "request"})
        return


mt5_client = MT5Client()
