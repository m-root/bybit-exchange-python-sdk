import hmac
import hashlib
import requests
import time
import base64
import random
import string


class Bybit():
    def __init__(self, base_url='https://api.bybit.com/v2/'):
        self.base_url = base_url

    def auth(self, key, secret):
        self.key = bytes(key, 'utf-8')
        self.secret = bytes(secret, 'utf-8')

    def order_link_id(self, stringLength):
        '''Alphanumeric random string generator'''
        lettersAndDigits = string.ascii_letters + string.digits
        return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

    def public_request(self, method, api_url, params):
        '''Public Requests'''
        r_url = self.base_url + api_url
        try:
            r = requests.request(method, r_url, params=params)
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        if r.status_code == 200:
            return r.json()

    def get_signed(self, sig_str):
        '''Parameter signing using sha512'''
        sig_str = base64.b64encode(sig_str)
        signature = base64.b64encode(hmac.new(self.secret, sig_str, digestmod=hashlib.sha1).digest())
        return signature

    def signed_request(self, method, api_url, params):
        '''Handler for a signed requests'''

        param = ''
        if params:
            sort_pay = sorted(params.items())
            # sort_pay.sort()
            for k in sort_pay:
                param += '&' + str(k[0]) + '=' + str(k[1])
            param = param.lstrip('&')
        timestamp = str(int(time.time() * 1000))
        full_url = self.base_url + api_url

        if method == 'GET':
            if param:
                full_url = full_url + '?' + param
            sig_str = method + full_url + timestamp
        elif method == 'POST':
            sig_str = method + full_url + timestamp + param

        signature = self.get_signed(bytes(sig_str, 'utf-8'))

        headers = {
            'FC-ACCESS-KEY': self.key,
            'FC-ACCESS-SIGNATURE': signature,
            'FC-ACCESS-TIMESTAMP': timestamp

        }

        try:
            r = requests.request(method, full_url, headers=headers, json=params)

            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
            print(r.text)
        if r.status_code == 200:
            return r.json()

    def get_symbols(self):
        '''Get all symbols in the API'''
        return self.public_request('GET', 'public/symbols')['result']

    def get_klines(self, symbol, interval, startTime, **kwargs):
        '''Getting a particular coin's kline'''
        params = {"symbol": symbol, "interval": interval, 'from': startTime}
        params.update(kwargs)
        return self.public_request('GET', 'public/kline/list', params)['result']

    def create_order(self, **params):
        '''Order Creation Support'''
        return self.signed_request('POST', 'private/order/create', **params)

    def buy(self, symbol, qty, price, amount):
        '''Market Buying of a coin'''
        return self.create_order(symbol=symbol, side='Buy', type='Market', qty=str(qty), price=str(price),
                                 time_in_force="GoodTillCancel", order_link_id=self.order_link_id(stringLength=6))

    def sell(self, symbol, price, amount):
        '''Market Selling of a coin'''
        return self.create_order(symbol=symbol, side='Sell', type='Market', qty='qty', price=str(price),
                                 time_in_force="GoodTillCancel", order_link_id=self.order_link_id(stringLength=6))

    def buyLimit(self, symbol, qty, price, amount):
        '''Limit Buying of a coin'''
        return self.create_order(symbol=symbol, side='Buy', type='Limit', qty=str(qty), price=str(price),
                                 time_in_force="GoodTillCancel", order_link_id=self.order_link_id(stringLength=6))

    def sellLimit(self, symbol, price, amount):
        '''Limit Buying of a coin'''
        return self.create_order(symbol=symbol, side='Sell', type='Limit', qty='qty', price=str(price),
                                 time_in_force="GoodTillCancel", order_link_id=self.order_link_id(stringLength=6))

    def cancel_order(self, order_id):
        '''Order cancellation'''
        return self.signed_request('POST', 'order/cancel', order_id)
