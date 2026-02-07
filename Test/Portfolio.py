import csv

from PortfolioStock import Stock
from StockPriceService import StockPriceService


def getStocks(filename):
    stocks=[]
    try:
        print(f" Begin Reading file into Stocks {filename}")

        with open(filename, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                stock = Stock(line[0],float(line[1]),float(line[2]))
                print(f"Stock Code is {stock.code}. Stock shares {stock.shares}. Stock Cost {stock.cost_per_share}")
                stocks.append(stock)
        return stocks
    except FileNotFoundError:
        print(f" Sorry your file {filename} doesnt exists ")
    print(f" Completed Reading files into Stocks -  {len(stocks)}")

## This method is going to call APIs to get the price for each of the stock in put it in Stock object
def populatePrices(my_portfolio_stock_list):
    print(f" Begin populating current price against each stock in portfolio {len(my_portfolio_stock_list)}")
    for my_stock_in_list in my_portfolio_stock_list:
        my_stock_in_list.current_price = StockPriceService.get_latest_price(my_stock_in_list.code,my_stock_in_list.cost_per_share)

    print(f" Completed populating current price against each stock in portfolio {len(my_portfolio_stock_list)}")
    return my_portfolio_stock_list

def computePortfolioData(my_portfolio_stock_list):
    print(" Begin computing portfolio data now... ")
    for stock in my_portfolio_stock_list:
        stock.total_cost = stock.shares*stock.cost_per_share
        stock.total_current_value = stock.shares*stock.current_price
        stock.profit_or_loss = stock.total_current_value - stock.total_cost
    print(" Completed computing portfolio data now... ")
    return my_portfolio_stock_list

##get File from user
portfolio_file_name = input("Please enter your portfolio file name: ")

portfolio_stocks = getStocks(portfolio_file_name)

##get the prices for each of the stock
portfolio_stocks_with_current_prices = populatePrices(portfolio_stocks)

##Now compute portfolio value and profit and loss
portfolio_stocks_with_portfolio_data =  computePortfolioData(portfolio_stocks_with_current_prices)

for stock in portfolio_stocks_with_current_prices:
    print(f" Stock {stock.code} Total cost is {stock.total_cost}  Current Value is {stock.total_current_value } and Net Gain is {stock.profit_or_loss}")






