from .order_manager import send_limit_order


class Order:
    def __init__(self, instrument, direction, tolerance):
        self.ticker = 0
        self.status = 0
        self.instrument = instrument
        self.tolerance = tolerance
        self.direction = direction
        self.side = "BUY"
        if self.direction == 2:
            self.side = "SELL"
        self.price = None
        self.desired_price = None
        self.desired_amount = None
        self.min_open_amount = 0.01
        self.price_round_to = 3
        self.amount_round_to = 2

    def update(self, desired_price, desired_amount):
       # print("update ", price, amount)
        if self.price is None and desired_price is not None:
            self.price = desired_price
            self.amount = desired_amount
            if desired_amount >= self.min_open_amount:
                print("setup order direction        ",
                      self.side, " price ", self.price)
                send_limit_order(self.instrument.symbol,
                                 self.price, self.amount)
            return

        self.desire_price = desired_price
        self.desired_amount = desired_amount

        if desired_price is not None:
            if abs(self.price - self.desire_price) > self.instrument.pips*self.tolerance:
                self.price = self.desire_price
                if desired_amount >= self.min_open_amount:
                    print("should update order direction",
                          self.side, " price ", desired_price)
                send_limit_order(self.instrument.symbol,
                                 self.price, self.amount)
