from datetime import datetime
import time
import MetaTrader5 as mt5


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
        return (ticker.bid, ticker.ask, ticker.time_msc)


mt5_client = MT5Client()
