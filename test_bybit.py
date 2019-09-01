import pytest
import os
from bybit import Bybit

KEY = os.environ['BTKEY']
SECRET = os.environ['BTSECRET']

bt = Bybit()
bt.auth(KEY, SECRET)

@pytest.mark.parametrize("bt",[(bt)])
def test_get_symbols(bt):
    assert len(bt.get_symbols()) > 0
    
@pytest.mark.parametrize("bt",[(bt)])
def test_get_klines(bt):
    klines = bt.get_klines('BTCUSD', '15', '1563367231')
    print(klines)
    print(f'len klines: {len(klines)}')

if __name__ == "__main__":
    test_get_klines(bt)