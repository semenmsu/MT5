import enum


DIR_LONG = 1
DIR_BUY = 1

DIR_SHORT = 2
DIR_SELL = 2

# order types, ENUM_ORDER_TYPE
ORDER_TYPE_BUY = 0  # Market Buy order
ORDER_TYPE_SELL = 1  # Market Sell order
ORDER_TYPE_BUY_LIMIT = 2  # Buy Limit pending order
ORDER_TYPE_SELL_LIMIT = 3  # Sell Limit pending order
ORDER_TYPE_BUY_STOP = 4  # Buy Stop pending order
ORDER_TYPE_SELL_STOP = 5  # Sell Stop pending order
# Upon reaching the order price, a pending Buy Limit order is placed at the StopLimit price
ORDER_TYPE_BUY_STOP_LIMIT = 6
# Upon reaching the order price, a pending Sell Limit order is placed at the StopLimit price
ORDER_TYPE_SELL_STOP_LIMIT = 7
ORDER_TYPE_CLOSE_BY = 8  # Order to close a position by an opposite one


# ENUM_TRADE_REQUEST_ACTIONS, Trade Operation Types
# Place a trade order for an immediate execution with the specified parameters (market order)
TRADE_ACTION_DEAL = 1
# Place a trade order for the execution under specified conditions (pending order)
TRADE_ACTION_PENDING = 5
TRADE_ACTION_SLTP = 6  # Modify Stop Loss and Take Profit values of an opened position
TRADE_ACTION_MODIFY = 7  # Modify the parameters of the order placed previously
TRADE_ACTION_REMOVE = 8  # Delete the pending order placed previously
TRADE_ACTION_CLOSE_BY = 10  # Close a position by an opposite one


# ENUM_ORDER_TYPE_TIME
ORDER_TIME_GTC = 0  # Good till cancel order
ORDER_TIME_DAY = 1  # Good till current trade day order
ORDER_TIME_SPECIFIED = 2  # Good till expired order
# The order will be effective till 23:59:59 of the specified day. If this time is outside a trading session,
ORDER_TIME_SPECIFIED_DAY = 3


# ENUM_ORDER_TYPE_FILLING
ORDER_FILLING_FOK = 0
ORDER_FILLING_IOC = 1
ORDER_FILLING_RETURN = 2
