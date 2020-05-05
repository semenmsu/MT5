from .constants import *
from .order_manager import send_limit_order


class BasePair:
    def __init__(self, symbol):
        self.symbol = symbol
        pass


class BasePrice:
    def __init__(self, contract):
        self.min = contract.min
        self.max = contract.max
        self.step = contract.step
        self.digits = contract.digits
        self.price = None

    def __call__(self, price=None):
        if price is not None:
            self.price = round(price, self.digits)
        return self

    def update(self, price=None):
        if price is not None:
            self.price = price
        return self

    @property
    def value(self):
        return round(self.price, self.digits)

    def add(self, pips=None, points=None):
        if pips is not None:
            self.price -= pips*self.step
        if points is not None:
            self.price -= points*self.step
        return self

    def minus(self, pips=None, points=None):
        if pips is not None:
            self.price -= pips*self.step
        if points is not None:
            self.price -= points*self.step
        return self


class BuyLimitOrder:
    def __init__(self, contract, tolerance=None):
        self.ticker = 0
        self.status = 0
        self.contract = contract
        if tolerance is None:
            tolerance = contract.step
        else:
            self.tolerance = tolerance

        self.direction = DIR_LONG
        self.side = "BUY"
        self.price = None
        self.desired_price = None
        self.desired_amount = None
        self.min_open_amount = 0.01
        self.price_round_to = contract.digits
        self.amount_round_to = contract.amount_digits

    def update(self, desired_price, desired_amount):
       # print("update ", price, amount)
        if self.price is None and desired_price is not None:
            self.price = desired_price
            self.amount = desired_amount
            if desired_amount >= self.min_open_amount:
                print("setup order direction        ",
                      self.side, " price ", self.price)
                send_limit_order(self.contract.symbol,
                                 self.price, self.amount)
            return

        self.desire_price = desired_price
        self.desired_amount = desired_amount

        if desired_price is not None:
            if abs(self.price - self.desire_price) > self.contract.pips*self.tolerance:
                self.price = self.desire_price
                if desired_amount >= self.min_open_amount:
                    print("should update order direction",
                          self.side, " price ", desired_price)
                send_limit_order(self.contract.symbol,
                                 self.price, self.amount)

    def __call__(self, desired_price, desired_amount):
        self.update(desired_price, desired_amount)


class Contract:

    def __init__(self, pair, suffix, min_price, max_price, step, price_digits, amount_digits):
        self.pair = pair
        self.suffix = suffix
        self.symbol = self.pair.symbol+self.suffix
        self.min = min_price
        self.max = max_price
        self.step = step
        self.pips = step
        self.digits = price_digits
        self.amount_digits = amount_digits

    def Price(self):
        return BasePrice(self)

    def BuyLimitOrder(self, tolerance=None):
        return BuyLimitOrder(self, tolerance)


EURUSDm = Contract(BasePair("EURUSD"), "m", 0, 10000, 0.00001, 5, 2)
USDJPYm = Contract(BasePair("USDJPY"), "m", 0, 10000, 0.001, 3, 2)
