#First install requests package ... File -- Setting--Project--Packages requests
# Secondly get the API Key  from https://www.alphavantage.co/support/#api-key
# To Test API key put the key in this URL and run it from browser https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=AAPL&apikey=FBZY4H5M9DW404UZ
# Documentation of API is https://www.alphavantage.co/documentation/#dailyadj

import requests

from StockPriceService import StockPriceService


def get_latest_price(stock_symbol):

    return 10.0

    url2 = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock_symbol}&apikey=FBZY4H5M9DW404UZ'
    response = requests.get(url2)
    print(response.text)

    stock_price_data = response.json()

    price_string = stock_price_data["Global Quote"]["05. price"]

    print(stock_price_data)
    latest_close = float(price_string)
    print(f" Latest close price as float is {latest_close}")
    return latest_close

price = get_latest_price("AAPL")
print (price)
get_latest_price("NVDA")
print (price)

price = StockPriceService.get_latest_price("IBM")
print(price)
