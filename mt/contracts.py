class BasePair:
    def __init__(self, symbol):
        self.symbol = symbol
        pass


class Contract:
    def __init__(self, pair, suffix):
        self.pair = pair
        self.suffix = suffix
        self.symbol = self.pair.symbol+self.suffix


EURUSDm = Contract(BasePair("EURUSD"), "m")
USDJPYm = Contract(BasePair("USDJPY"), "m")
