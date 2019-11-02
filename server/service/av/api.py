'''
API to communicate with alphavantage
'''
import os
import requests

from . import const

API_KEY = os.getenv('API_KEY_ALPHAVANTAGE')

BASE_URL = 'https://www.alphavantage.co/query'

def query(
    function=None,
    symbol=None,
    interval=None,
    full=False,
):
    if None in [function, symbol]:
        raise RuntimeError('function and symbol required')

    params = {
        'apikey': API_KEY,
        'function': const.AV_Function_param_map[function],
        'symbol': symbol.upper(),
    }

    if interval is not None:
        params['interval'] = f'{interval}min',

    if full:
        params['outputsize']: 'full'

    try:
        resp = requests.get(BASE_URL, params=params)
    except requests.RequestException as e:
        raise RuntimeError('request exception,', e)

    data = resp.json()

    if 'Error Message' in data:
        raise RuntimeError('received response error', data)

    return data
