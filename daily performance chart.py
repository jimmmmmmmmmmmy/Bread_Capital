import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv('alt banger explainations/daily_performance.csv')

hfont = {'fontname': 'Helvetica Neue'}

df['date'] = pd.to_datetime(df['date'])

fig, ax = plt.subplots(figsize=(15, 8))

df['strategy_cum_log_ret_3x'] = df['strategy_cum_log_ret'] * 3

ax.plot(df['date'], df['buy_hold_cum_log_ret_nq'], color='blue', label='Benchmark (Nasdaq-100)')
ax.plot(df['date'], df['strategy_cum_log_ret'], color='turquoise', label='Bread Capital')
ax.plot(df['date'], df['strategy_cum_log_ret_3x'], color='limegreen', label='Bread Capital (3x)')

ax.set_xlabel('Date', **hfont)
ax.set_ylabel('Cumulative Log Return', **hfont)
ax.set_title('Daily Performance: Bread Capital vs Benchmark (Nasdaq-100)', **hfont)

# format the x-axis tick labels to display the date
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

# add more x-ticks
ax.set_xticks(pd.date_range(start=df['date'].min(), end=df['date'].max(), freq='M'))

plt.xticks(rotation=60, **hfont)

# hoizontal grey stripes
y_min, y_max = ax.get_ylim()
y_range = np.arange(-.2, 1, .1)
for y in y_range:
    ax.axhline(y, color='gray', linestyle='--', linewidth=0.15, zorder=0)
    
# legend with font
ax.legend(prop={'family': 'Helvetica Neue'})

plt.tight_layout()

plt.show()
