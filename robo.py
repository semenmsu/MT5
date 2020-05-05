from datetime import datetime
import time
import MetaTrader5 as mt5
from mt.constants import *
from mt.contracts import USDJPYm
from mt.instrument import Instrument
from mt.order import Order


class Session:
    def __init__(self):
        self.instruments = dict()

    def Instrument(self, contract):
        if contract in self.instruments:
            return self.instruments[contract]

        self.instruments[contract] = Instrument(contract)
        return self.instruments[contract]

    def is_valid(self):
        for instrument in self.instruments.values():
            if not instrument.is_valid():
                return False
        return True

    def update(self):
        for instrument in self.instruments.values():
            instrument.update()


class Robo:
    def __init__(self, contract):
        self.contract = contract
        self.session = Session()
        self.instrument = self.session.Instrument(contract)
        self.running = False
        self.mm_bid = contract.Price()
        self.mm_bid_amount = 0.01
        self.mm_ask = contract.Price()
        self.mm_ask_amount = 0
        self.price_tolerance = 3
        self.position = 0
        #self.long = Order(self.instrument, DIR_LONG, self.price_tolerance)
        self.buy_limit = contract.BuyLimitOrder(self.price_tolerance)
        self.short = Order(self.instrument, DIR_SHORT, self.price_tolerance)

    def run(self):
        self.running = True
        instrument = self.instrument
        mm_bid = self.mm_bid
        mm_ask = self.mm_ask

        while self.running:
            self.session.update()
            if self.session.is_valid():
                mm_bid.update(instrument.bid).minus(points=10)
                mm_ask.update(instrument.ask).add(points=10)
                self.buy_limit(mm_bid.value, self.mm_bid_amount)
            time.sleep(1)


robo = Robo(USDJPYm)

robo.run()
