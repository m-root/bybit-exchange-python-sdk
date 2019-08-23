import os
from bybit import Bybit

KEY = os.environ['BTKEY']
SECRET = os.environ['BTSECRET']


def test_connection():
    bt = Bybit()
    bt.auth(KEY, SECRET)
    return bt

bt = test_connection()

def test_get_symbols(bt):
    assert bt.get_symbols().status == 200
