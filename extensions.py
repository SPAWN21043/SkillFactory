import requests
import json
from config import keys


class APIException(Exception):
    pass


class Converter:
    @staticmethod
    def get_price(valeus):
        if len(valeus) != 3:
            raise APIException('Не верное количество параметров')

        quote, base, amount = valeus

        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_tiker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}.')

        try:
            base_tiker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}.')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://free.currconv.com/api/v7/convert?q={quote_tiker}_{base_tiker}&compact=ultra&apiKey=3b6d9226d0dcf84f55fd')
        tikers = (f'{keys[quote]}_{keys[base]}')
        result = float(json.loads(r.content)[tikers])*amount

        return round(result, 3)