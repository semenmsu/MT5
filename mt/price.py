class Price:
    def __init__(self, contract):
        self.min = min_
        self.max = max_
        self.step = step
        self.digits = digits
        self.price = None

    def __call__(self, price=None):
        if price is not None:
            self.price = round(price, self.digits)
        return self

    @property
    def value(self):
        return round(self.price, self.digits)

    def add(self, pips):
        if self.price is not None:
            self.price += pips*self.step

    def minus(self, pips):
        if self.price is not None:
            self.price -= pips*self.step
