#First install requests package ... File -- Setting--Project--Packages requests
# Secondly get the API Key  from https://www.alphavantage.co/support/#api-key
# To Test API key put the key in this URL and run it from browser https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=AAPL&apikey=FBZY4H5M9DW404UZ
# Documentation of API is https://www.alphavantage.co/documentation/#dailyadj

from datetime import date

import requests

#History Prices

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&apikey=FBZY4H5M9DW404UZ'
r = requests.get(url)
data = r.json()
print(data)

#option 1
# Extract the nested dictionary
time_series = data["Time Series (Daily)"]
# Get the first available date key
first_date = next(iter(time_series))
# Access the "4. close" value for that date
first_close = time_series[first_date]["4. close"]
print(f" latest price for {first_date} is {first_close}")  # Output: 255.5300

#option 2
today = date.today().isoformat() # datetime.now().strftime("%Y-%m-%d")          # "2026-01-17"
if today in data["Time Series (Daily)"]:
    close = float(data["Time Series (Daily)"][0]["4. close"])
    print(f"Close on {today}: ${close:.2f}")  # Close on 2026-01-16: $255.53
else:
    print("Market data for today not available yet (weekend/holiday?)")


