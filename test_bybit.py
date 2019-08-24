import pytest
import os
from bybit import Bybit

KEY = os.environ['BTKEY']
SECRET = os.environ['BTSECRET']

bt = Bybit()
bt.auth(KEY, SECRET)


def test_get_symbols(bt):
    assert bt.get_symbols().status == 200