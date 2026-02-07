import csv

from PortfolioStock import Stock
from StockPriceService import StockPriceService
from StockPriceUtil import StockPriceUtil


class PortfolioManager:

    def __init__(self):
        print(" Portfolio Manager has been instantiated ")


    def readPortfolio(self, filename):
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
    def populatePrices(self,my_portfolio_stock_list):
        print(f" Begin populating current price against each stock in portfolio {len(my_portfolio_stock_list)}")
        stock_price_util = StockPriceUtil()
        for my_stock_in_list in my_portfolio_stock_list:
            my_stock_in_list.current_price = StockPriceService.get_latest_price(my_stock_in_list.code,my_stock_in_list.cost_per_share)
            my_stock_in_list.year_high = stock_price_util.get52WkHigh(my_stock_in_list.code)

        print(f" Completed populating current price against each stock in portfolio {len(my_portfolio_stock_list)}")
        return my_portfolio_stock_list

    def computePortfolioData(self,my_portfolio_stock_list):
        print(" Begin computing portfolio data now... ")
        for stock in my_portfolio_stock_list:
            stock.total_cost = stock.shares*stock.cost_per_share
            stock.total_current_value = stock.shares*stock.current_price
            stock.profit_or_loss = stock.total_current_value - stock.total_cost
        print(" Completed computing portfolio data now... ")
        return my_portfolio_stock_list

    def  printPortfolio(self,portfolio):
        for stock in portfolio:
            print(f" Stock {stock.code} Total cost is {stock.total_cost} Shares  Current Price is {stock.current_price} Current Value is {stock.total_current_value } Net Gain is {stock.profit_or_loss} and 52W High is {stock.year_high}.")

    def generatePortfolioReport(self,portfolio, portfolio_file_name):
        try:
            print("Generating report ")
            with open(f"report_{portfolio_file_name}", mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Code","Cost/Share", "Shares", "Total Cost", "Current Price" , "Total Current Value","Profit or Loss"])
                for stock in portfolio:
                    writer.writerow([stock.code,stock.cost_per_share, stock.shares, stock.total_cost,stock.current_price, stock.total_current_value,stock.profit_or_loss,stock.year_high])
        except Exception as error:
            print("Failed to generate report ",error)


    def processPortfolio(self, portfolio_file_name):

        ##read File and create list of Stock objects
        print("Read Portfolio file ",portfolio_file_name)
        portfolio = self.readPortfolio(portfolio_file_name)

        print(f"Get prices for stocks in portfolio. Total number of stocks in portfolio are {len(portfolio)} ")
        ##get the prices for each of the stock
        portfolio = self.populatePrices(portfolio)

        print(f"Compute portfolio data using latest prices. Total number of stocks in portfolio are {len(portfolio)} ")
        ##Now compute portfolio value and profit and loss
        portfolio =  self.computePortfolioData(portfolio)
        self.generatePortfolioReport(portfolio,portfolio_file_name)
        self.printPortfolio(portfolio)





