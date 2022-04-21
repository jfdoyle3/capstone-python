def get_data():
    from requests import Request, Session
    from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
    import json
    ticker_url='https://api.nomics.com'
    endpoint='/v1/currencies/ticker'
    parameters = {
          'key':'8381f81057e8766c11cd0109bae84864',
          'ids': 'BTC'
            }
    headers={
         'Accepts': 'application/json'
         }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(ticker_url+endpoint, params=parameters)
        results = json.loads(response.text)

    except (ConnectionError, Timeout, TooManyRedirects) as e:
          print(e)
    return results

def process():
    data=get_data()
    return data[0]
