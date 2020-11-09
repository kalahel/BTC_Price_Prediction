from binance.client import Client
import pandas as pd

credentials = pd.read_csv('credentials.csv')

client = Client(credentials['api_key'][0], credentials['api_secret'][0])
bars = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1HOUR, "1 day ago UTC")
print(bars)

for line in bars:
    del line[5:]

pd.set_option('display.max_rows', 1000)
btc_df = pd.DataFrame(bars, columns=['date', 'open', 'high', 'low', 'close'])
btc_df.set_index('date', inplace=True)

print(btc_df)
btc_df.to_csv('./datasets/btcToUSDT1h.csv')
