import pandas as pd
import matplotlib
from datetime import datetime
import time
import matplotlib.pyplot as plt

csv_file_name = 'btcToUSDT1h.csv'
df = pd.read_csv('./datasets/' + csv_file_name)

total_time_laps = (df['date'][len(df['date']) - 1] - df['date'][0])
mean_time_laps = total_time_laps / len(df['date'])

# Print in hh:mm:ss if possible else print in days
print('Total number of rows : ',
      len(df['date']),
      '\nStart date : ',
      datetime.fromtimestamp(int(df['date'][0] / 1000)),
      '\nElapsed time in dataset : ',
      (total_time_laps / (1000 * 3600 * 24)) if
      (total_time_laps / 1000 > 86399) else
      time.strftime('%H:%M:%S', time.gmtime(total_time_laps / 1000)),
      '\nMean elapsed time between data: ',
      ((mean_time_laps / (1000 * 3600 * 24)) if
       (mean_time_laps / 1000 > 86399) else
       time.strftime('%H:%M:%S', time.gmtime(mean_time_laps / 1000))) if
      (mean_time_laps > 1000) else
      (str(mean_time_laps) + ' ms')
      )

# Changin date to days
df['date'] = [((x - df['date'][0]) / (1000 * 3600 * 24)) for x in df['date']]

fig, ax = plt.subplots()
ax.plot(df['date'], df['open'])
# ax.plot(df['date'][11:len(df['date'])], df['open'][11:len(df['date'])])
# ax.plot(df['open'])


ax.set(xlabel='time (day)', ylabel='UDS',
       title='BTC in USD')
ax.grid()

fig.savefig("test.png")
plt.show()
