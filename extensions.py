import requests
import json
from confing import keys






class ConvertionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price (quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException(f'Невозможно перевисти одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не существующая волюта валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не существующая волюта валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не правильное количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return  total_base
