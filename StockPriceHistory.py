import csv
from stock import Stock
import yfinance as yf
from DBService import DBService  # Import your DB service

class StockPriceHistory:

    def __init__(self, portfolio_file):
        self.stocks = []
        with open(portfolio_file, 'r') as f:
            for line in csv.reader(f):
                self.stocks.append(Stock(line[0], int(line[1]), float(line[2])))

    def run(self):
        choice = input("Would you like to see the value of your portfolio from any date in the past? (yes/no): ").lower()
        if choice == "yes":
            start_date = input("Enter start date (YYYY-MM-DD): ")
            history = {}  # Will store portfolio values for each date

            # Fetch historical prices and calculate portfolio value
            for stock in self.stocks:
                data = yf.Ticker(stock.code).history(start=start_date)
                for i in range(len(data)):
                    date = data.index[i]  # Date at the i'th index
                    date_str = str(date.date())  # Convert to YYYY-MM-DD
                    close_price = data.values[i][3]  # Close price

                    if date_str in history:
                        history[date_str] += stock.shares * close_price
                    else:
                        history[date_str] = stock.shares * close_price

            # Write CSV
            csv_file_name = "portfolio_history.csv"
            with open(csv_file_name, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Date", "Portfolio Value"])
                for date in sorted(history):
                    writer.writerow([date, round(history[date], 2)])

            print(f"Portfolio history saved to {csv_file_name}")


            create_table_query = """
            CREATE TABLE IF NOT EXISTS portfolio_history (
                portfolio_date DATE PRIMARY KEY,
                portfolio_value FLOAT
            )
            """
            DBService.execute_query(create_table_query)

            for date, value in history.items():
                insert_query = f"""
                INSERT INTO portfolio_history (portfolio_date, portfolio_value)
                VALUES ('{date}', {round(value, 2)})
                """
                DBService.execute_query(insert_query)

            print("Portfolio history values inserted into database successfully.")

        else:
            print("Skipped portfolio history.")