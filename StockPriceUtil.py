import yfinance as yf

class StockPriceUtil:

    #def __init__(self):
    #    print( " Yahoo finance API to get finance data for free ")

    def getLatestPrice(self, ticker):
        #print(" Request to get latest price for given stock ", ticker)
        tickerDetails = yf.Ticker(ticker)
        price = tickerDetails.info["regularMarketPrice"]
        print(f"The price from Yahoo finance for stock {ticker} is {price}")
        return price

    def get52WkHigh(self, ticker):
        print(" Request to get  price for given stock ", ticker)
        tickerDetails = yf.Ticker(ticker)
        #print(tickerDetails)
        #print(tickerDetails.financials)
        #print(tickerDetails.info)
        #print(tickerDetails.info["regularMarketPrice"])
        return tickerDetails.info["fiftyTwoWeekHigh"]



##stkprice = StockPriceUtil()

##while True:
##    ticker = input("What stock are you looking for? ")
##    price = stkprice.getLatestPrice(ticker)
##   print(f" The price of stock {ticker} is  {price}")
##    print(f" The 52 week high price of stock {ticker} is  {stkprice.get52WkHigh(ticker)}")
####