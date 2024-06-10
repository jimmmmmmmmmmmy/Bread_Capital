import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MaxNLocator
import numpy as np

df = pd.read_csv('alt banger explainations/bread_strategy.csv')

df['time'] = pd.to_datetime(df['time'], unit='s')

fig, ax = plt.subplots(figsize=(15, 8))

ax.plot(df.index, df['buy_hold_cum_log_ret_nq'], label='Buy and Hold', color='blue')

df['strategy_cum_log_ret_3x'] = df['strategy_cum_log_ret'] * 2.95

ax.plot(df.index, df['strategy_cum_log_ret'], label='Strategy', color='turquoise')
ax.plot(df.index, df['strategy_cum_log_ret_3x'], label='Strategy 3x', color='limegreen')

y_min, y_max = ax.get_ylim()
y_range = np.arange(-.2, .9, .05)
for y in y_range:
    ax.axhline(y, color='gray', linestyle='--', linewidth=0.1, zorder=0)

x_min, x_max = ax.get_xlim()
x_range = np.arange(0, 40000, 2500)
for x in x_range:
    ax.axvline(x, color='gray', linestyle='--', linewidth=0.1, zorder=0)

ax.set_xlabel('Trade Number', fontname='Helvetica Neue')
ax.xaxis.set_major_locator(MaxNLocator(integer=True))

ax.set_ylabel('Cumulative Log Return', fontname='Helvetica Neue')

plt.title('Performance by Strategy Trade: Bread Capital vs Benchmark (Nasdaq-100)', fontname='Helvetica Neue')

ax.legend(fontsize=10, prop={'family': 'Helvetica Neue'})

plt.tight_layout()

plt.show()
