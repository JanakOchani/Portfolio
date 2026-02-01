from email.policy import default

import requests

from PortfolioEnvironment import PortfolioEnvironment
from StockPriceUtil import StockPriceUtil


class StockPriceService:

    def get_latest_price(stock_symbol, default_price=0):
        try:
            env = PortfolioEnvironment()
            api_url = env.getProperty("api_url")
            api_key=env.getProperty("api_key")
            url2 = f'{api_url}{stock_symbol}&apikey={api_key}'
            response = requests.get(url2)
            print(response.text)
            stock_price_data = response.json()
            price_string = stock_price_data["Global Quote"]["05. price"]
            print(stock_price_data)
            latest_close = float(price_string)
            print(f" Latest close price as float is {latest_close}")
            return latest_close
        except:
            print("  MY APIs are not working, Let me try to get the price from yahoo ")
            stkpriceutil = StockPriceUtil()
            return stkpriceutil.getLatestPrice(stock_symbol)
            #return default_price*1.25 #this is just to move on.. we need to remove this before going live