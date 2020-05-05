"""
Example simple spreader robot for MetaTrader5
using python API
"""

import time
import logging
from mt.contracts import USDJPYm
from mt.instrument import Instrument


class Session:
    """
    Session contains all instruments for trading and check validity
    """

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
    """
    Spreader example
    """

    def __init__(self, contract):
        self.contract = contract
        self.session = Session()
        self.instrument = self.session.Instrument(contract)
        self.running = False
        self.mm_bid = contract.Price()
        self.mm_bid_amount = 0.01
        self.mm_ask = contract.Price()
        self.mm_ask_amount = 0.01
        self.price_tolerance = 3
        self.position = 0  # contract.Position()
        self.buy_limit = contract.BuyLimitOrder(self.price_tolerance)
        self.sell_limit = contract.SellLimitOrder(self.price_tolerance)
        self.needs_updating = True

    def update(self):
        self.session.update()
        if self.session.is_valid():
            self.mm_bid.update(self.instrument.bid).minus(points=10)
            self.mm_ask.update(self.instrument.ask).add(points=10)
            self.buy_limit.update(self.mm_bid.value, self.mm_bid_amount)
            self.sell_limit.update(self.mm_ask.value, self.mm_ask_amount)
        else:
            self.handle_not_valid_session()

    def handle_not_valid_session(self):
        print("handle_not_valid_session is not implemented")

    def should_be_updated(self):
        self.needs_updating = True

    def run(self):
        self.running = True
        while self.running:
            self.update()
            time.sleep(0.1)


robo = Robo(USDJPYm)

robo.run()
