
# bybit-exchange-python-sdk
This is an unofficial Bybit Exchange API python implementation for automated trading. Find the documentation [here](https://bybit-exchange.github.io/bybit-official-api-docs/en/index.html).


Features
--------

- Implementation of all General, Market Data and Account endpoints.
- Simple handling of authentication
- No need to generate timestamps yourself, the wrapper does it for you
- Response exception handling
- Historical Kline/Candle fetching function


Quick Start
-----------

To register an account with Bybit [Click here](https://www.bybit.com/app/register?ref=00xv5)

To Generate an API Key  and assign relevant permissions [Click here](https://www.bybit.com/app/user/api-management) 


**Python**

    from bybit import Bybit
    client = Client(api_key, api_secret)

    # get exchange symbols
    depth = Bybit().get_symbols()

    
    # get all symbol prices
    prices = Bybit().get_klines('BTCUSD', '15', '1563367231')

    
    # Create Market Buy Orders
    auth = Bybit().auth(key, secret)
    prices = buy('BTCUSD', 9550, 1.000)

    

    
    # Create Market Sell Orders
    auth = Bybit().auth(key, secret)
    prices = buy('BTCUSD', 9550, 1.000)

    

    
    # Create Market Buy Limit Orders
    auth = Bybit().auth(key, secret)
    prices = buy('BTCUSD', 9550, 1.000)

    

    
    # Create Market Sell Limit Orders
    auth = Bybit().auth(key, secret)
    prices = buy('BTCUSD', 9550, 1.000)

    

    
    # Cancelling an order
    auth = Bybit().auth(key, secret)
    prices = cancel_order(order_id)
    




For more check out the documentation 

    https://bybit-exchange.github.io/bybit-official-api-docs/en/index.html

