import time

from binance.client import Client
import pandas as pd

NUMBER_OF_BATCHES = 10
DAYS_PER_BATCH = 40
credentials = pd.read_csv('credentials.csv')
client = Client(credentials['api_key'][0], credentials['api_secret'][0])

for i in range(0, NUMBER_OF_BATCHES):
    print("Retrieving : ", i + 1, "/", NUMBER_OF_BATCHES)
    # this method return data from oldest to newest
    temps_bars = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1HOUR,
                                              str((DAYS_PER_BATCH * (NUMBER_OF_BATCHES - i)) + 1) + " day ago UTC",
                                              str((DAYS_PER_BATCH * (NUMBER_OF_BATCHES - i - 1)) + 1) + " day ago UTC")
    # Removing irrelevant data
    for line in temps_bars:
        del line[5:]
    if i == 0:
        btc_df = pd.DataFrame(temps_bars, columns=['date', 'open', 'high', 'low', 'close'])

    else:
        tmp_df = pd.DataFrame(temps_bars, columns=['date', 'open', 'high', 'low', 'close'])
        btc_df = btc_df.append(tmp_df)

btc_df.set_index('date', inplace=True)
btc_df.to_csv('./datasets/btc_to_USDT_1h_' + str(NUMBER_OF_BATCHES * DAYS_PER_BATCH) + '_d.csv')
