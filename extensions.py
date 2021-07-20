import json
import requests
from config import keys
class ConvertionException(Exception):
    pass

class CryptoConverter():
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f'Невозможно конвертировать одну и ту же валюту {base}')
        if quote not in keys.keys():
            raise ConvertionException(f'Неверный ввод {quote}')
        elif base not in keys.keys():
            raise ConvertionException(f'Неверный ввод {base}')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')
        try:
            amount = float(amount)
            if amount < 3:
                raise ConvertionException('Неправильно указаны параметры запроса.')
        except ValueError:
            raise ConvertionException(f'Не удалось обработать кол-во {amount}')



        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]
        total_base = total_base * amount
        return total_base

