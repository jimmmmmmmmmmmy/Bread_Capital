import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('alt banger explainations/monthly performance.csv')

df['Month'] = pd.to_datetime(df['Month'])

df['strategy_percent_gains'] = pd.to_numeric(df['strategy_percent_gains'].str.rstrip('%'))
df['buy_hold_percent_gains'] = pd.to_numeric(df['buy_hold_percent_gains'].str.rstrip('%'))
df['strategy_percent_gains_3x'] = df['strategy_percent_gains'] * 2.95

fig, ax = plt.subplots(figsize=(15, 6))

# width of each bar
bar_width = 0.5

x_tick_distance = 2

# positions of the bars on the x-axis
r1 = range(0, len(df) * int(x_tick_distance), int(x_tick_distance))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]
 
# bars for each month
ax.bar(r1, df['buy_hold_percent_gains'], color='blue', width=bar_width, label='Benchmark (S&P 500)')
ax.bar(r2, df['strategy_percent_gains'], color='turquoise', width=bar_width, label='Bread Capital, 3t slippage, $2 comms')
ax.bar(r3, df['strategy_percent_gains_3x'], color='limegreen', width=bar_width, label='Bread Capital 3x w/ comms')

# x-tick labels and positions
plt.xticks([r + bar_width/2 for r in r1], df['Month'].dt.strftime('%Y-%m'), rotation=45, **hfont)

# y-axis limits based on the minimum and maximum percent gains
min_gain = min(df['strategy_percent_gains_3x'].min(), df['buy_hold_percent_gains'].min())
max_gain = max(df['strategy_percent_gains_3x'].max(), df['buy_hold_percent_gains'].max())
ax.set_ylim(min_gain - 1, max_gain + 1)

# horizontal grey bands
y_min, y_max = ax.get_ylim()
y_range = np.arange(-10, 15, 1)
for y in y_range:
    ax.axhline(y, color='gray', linestyle='--', linewidth=0.25, zorder=0)
    
# labels and title
ax.set_ylabel('Monthly Gain (%)', **hfont)
ax.set_title('Performance Overview (Modeled)', **hfont)


ax.legend(loc='lower right', prop={'family': 'Helvetica Neue'})

plt.tight_layout()

plt.show()
