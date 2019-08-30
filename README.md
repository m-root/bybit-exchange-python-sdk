bybit-exchange-python-sdk
=========================

[![CircleCI](https://circleci.com/gh/rgalbo/bybit-exchange-python-sdk.svg?style=svg)](https://circleci.com/gh/rgalbo/bybit-exchange-python-sdk)

This is an unofficial Bybit Exchange API python implementation for automated trading. [API Documentation](https://bybit-exchange.github.io/bybit-official-api-docs/en/index.html).

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

Installation
------------
`$ pip install .`

or for my purposes:

```
pyenv local 3.7.4
mkvirtualenv futures
workon futures
pip install -r requirements.txt
cd bybit
python -m pip install -e .
cd ..
jupyter lab
```

KEY Env Variables
-----------------
```
$ vi key_example.sh             # add your api key from bybit in the parenthesis
$ cp key_example.sh key.sh 
$ source key.sh                   # if this doesnt work, copy paste the two lines to your terminal
```

alternatively, in the disgust of all other failure you are likely to ask to just please god fucking hell make jupyter environments stop and run(see [jvp](https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/)):

for ipython:

```ipython
# follows conveintion %set_env var val:
%set_env BTKEY '[your_key_here]'
%set_env BTSECRET '[your_secret_here]'
```

for last resort, (key.py):

```python
import sys,os,os.path
sys.path.append(os.path.expanduser('~/code/eol_hsrl_python'))
os.environ['HSRL_INSTRUMENT']='gvhsrl'
os.environ['HSRL_CONFIG']=os.path.expanduser('~/hsrl_config')
```

API Usage Examples
------------------

```python
import os
from bybit import Bybit

KEY = os.environ['BTKEY']
SECRET = os.environ['BTSECRET']

bt = Bybit()
bt.(api_key, api_secret)

# get exchange symbols
depth = bt.get_symbols()

# get all symbol prices
prices = bt.get_klines('BTCUSD', '15', '1563367231')

# Create Market Buy Orders
prices = bt.buy('BTCUSD', 9550, 1.000)
```

check out the [documentation](https://bybit-exchange.github.io/bybit-official-api-docs/en/index.html)!

