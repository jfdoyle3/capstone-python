from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

ticker_url = 'https://api.nomics.com/v1/currencies/ticker'
parameters = {
    'key': '8381f81057e8766c11cd0109bae84864',
    'ids': 'BTC'
}
headers = {
    'Accepts': 'application/json'
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(ticker_url, params=parameters)
    results = json.loads(response.text)
    # data=results['data']
    print(json.dumps(results, sort_keys=True, indent=4))

except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
