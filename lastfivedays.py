import matplotlib.pyplot as plt
import yfinance
from datetime import date, timedelta

def getLastFiveDays():
    today = date.today()
    day_list = []
    
    while len(day_list) <= 5:
        if today.strftime("%a") == "Sat" or today.strftime("%a") == "Sun":
            pass
        else:
            day_list.append(today)
        
        today = today - timedelta(1)
    
    return day_list

def getClosingPrices(ticker):
    last_five_days = getLastFiveDays()
    
    stock = yfinance.Ticker(ticker)
    stock_historical = stock.history(start=last_five_days[4])
    
    closing_prices = stock_historical['Close']
    
    return closing_prices.to_numpy()

def getPercentChange(close_prices):
    pct_change = []
    
    one_day_change = ((close_prices[4]-close_prices[3])/close_prices[3]) * 100
    two_day_change = ((close_prices[4]-close_prices[2])/close_prices[2]) * 100
    three_day_change = ((close_prices[4]-close_prices[1])/close_prices[1]) * 100
    four_day_change = ((close_prices[4]-close_prices[0])/close_prices[0]) * 100
    
    pct_change.append(0)
    pct_change.append(one_day_change)
    pct_change.append(two_day_change)
    pct_change.append(three_day_change)
    pct_change.append(four_day_change)
    
    return pct_change

days = getLastFiveDays()
days.pop()

ticker_file = open("tickers.txt","r")
tickers = []

for ticker in ticker_file:
    ticker = ticker.rstrip()
    tickers.append(ticker)

ticker_file.close()

return_list = []

for i in tickers:
    
    close_prices = getClosingPrices(i)
    change = getPercentChange(close_prices)
        
    return_list.append(change)  

ctr = 0

for m in return_list:    
    plt.plot(days[::-1],m,label=tickers[ctr])
    
    ctr += 1

plt.legend()
plt.xticks(days)
plt.xticks(rotation=45)
plt.show()