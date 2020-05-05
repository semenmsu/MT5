from .mt5_client import mt5_client as client


class Instrument:
    def __init__(self, contract):
        self.contract = contract
        self.symbol = contract.symbol
        self.bid = None
        self.ask = None
        self.ts = None
        self.pips = 0.001

    def update(self):
        #[self.bid, self.ask, self.ts] = get_bid_ask(self.symbol)
        [self.bid, self.ask, self.ts] = client.ticker(self.symbol)

    def is_valid(self):
        return self.bid and self.ask

    def __repr__(self):
        return "%s %s %s" % (self.symbol, str(self.bid), str(self.ask))
