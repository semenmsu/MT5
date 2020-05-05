from datetime import datetime
import time
import MetaTrader5 as mt5
from mt.constants import *
from mt.contracts import USDJPYm
from mt.instrument import Instrument
from mt.order import Order


class Robo:
    def __init__(self, symbol):
        self.instrument = Instrument(symbol)
        self.running = False
        self.mm_bid = None
        self.mm_bid_amount = 0.01
        self.mm_ask = None
        self.mm_ask_amount = 0
        self.price_tolerance = 3
        self.position = 0

        self.long = Order(self.instrument, DIR_LONG, self.price_tolerance)
        self.short = Order(self.instrument, DIR_SHORT, self.price_tolerance)
        self.price_roundto = 3
        self.amount_roundto = 2

    def normalize_price(self, price):
        return round(price, self.price_roundto)

    def normalize_amount(self, amount):
        return round(amount, self.amount_roundto)

    def run(self):
        self.running = True
        while self.running:
            self.instrument.update()
            # print(self.instrument)
            if self.instrument.is_valid():
                self.mm_bid = self.normalize_price(
                    self.instrument.bid - 10*self.instrument.pips)
                self.mm_ask = self.normalize_price(
                    self.instrument.ask + 10*self.instrument.pips)
                self.long.update(self.mm_bid, self.mm_bid_amount)
            time.sleep(1)


robo = Robo(USDJPYm)

robo.run()
