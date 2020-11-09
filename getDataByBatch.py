from binance.client import Client
import pandas as pd

NUMBER_OF_DAYS = 10

credentials = pd.read_csv('credentials.csv')
client = Client(credentials['api_key'][0], credentials['api_secret'][0])

bars = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1HOUR, str(NUMBER_OF_DAYS) + " day ago UTC")

# Removing irrelevant data
for line in bars:
    del line[5:]
# Creating data frame
btc_df = pd.DataFrame(bars, columns=['date', 'open', 'high', 'low', 'close'])
btc_df.set_index('date', inplace=True)

# TODO optimize this for downloading batch of 1000 rows each time (actual 24)
for i in range(1, NUMBER_OF_DAYS):
    print("Retrieving : ", i, "/", NUMBER_OF_DAYS - 1)
    temps_bars = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1HOUR,
                                              str(NUMBER_OF_DAYS - i) + " day ago UTC")
    for line in temps_bars:
        del line[5:]
    btc_df.append(temps_bars)

btc_df.to_csv('./datasets/btc_to_USDT_1h_' + str(NUMBER_OF_DAYS) + '_d.csv')
