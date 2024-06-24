import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator, MONDAY
import matplotlib.dates as mdates

df = pd.read_csv('daily_performance.csv', parse_dates=['date'], index_col='date')

df['strategy_daily_return'] = df['strategy_cum_log_ret'].diff() * 10000

#benchmark_df['benchmark_daily'] = df['benchmark_perf'].diff() * 10000  # * 10000 to convert to basis points

df = df.merge(benchmark_df[['benchmark_daily']], left_index=True, right_index=True, how='left')

# Function to create a single plot
def create_plot(df, ax, start_date, end_date, title):
    df_period = df[(df.index >= start_date) & (df.index <= end_date)]
    
    dates = mdates.date2num(df_period.index)
    colors = ['navy' if r > 0 else 'darkblue' for r in df_period['strategy_daily_return']]
    
    ax.bar(dates, df_period['strategy_daily_return'], color=colors, width=1, align='center', edgecolor='none', label='Strategy Returns')
    
    #ax.bar(dates, df_period['benchmark_daily'], color='green', alpha=0.15, width=1, align='center', edgecolor='none', label='Benchmark Returns')
    
    ax.set_title(title, fontproperties=prop, fontsize=16)
    ax.set_xlabel('Date', fontproperties=propaxis, fontsize=10)
    ax.set_ylabel('Daily Return (bps)', fontproperties=prop, fontsize=10)
    
    locator = WeekdayLocator(byweekday=MONDAY, interval=2)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    ax.legend(prop=prop, fontsize=8)

def calculate_stats(df, start_date, end_date):
    df_period = df[(df.index >= start_date) & (df.index <= end_date)]
    
    total_days = len(df_period)
    total_years = (df_period.index.max() - df_period.index.min()).days / 365.25
    positive_returns = (df_period['strategy_daily_return'] > 0).sum()
    negative_returns = (df_period['strategy_daily_return'] < 0).sum()
    max_return = df_period['strategy_daily_return'].max()
    min_return = df_period['strategy_daily_return'].min()
    average_daily_return = df_period['strategy_daily_return'].mean()
    std_daily_return = df_period['strategy_daily_return'].std()
    daily_sharpe_ratio = average_daily_return / std_daily_return if std_daily_return != 0 else 0
    trading_days_per_year = 252
    annualized_sharpe_ratio = daily_sharpe_ratio * np.sqrt(trading_days_per_year)
    annualized_return = average_daily_return * trading_days_per_year
    annualized_volatility = std_daily_return * np.sqrt(trading_days_per_year)
    
    #benchmark_daily_return = df_period['benchmark_daily'].mean()
    #benchmark_std_daily_return = df_period['benchmark_daily'].std()
    #benchmark_daily_sharpe_ratio = benchmark_daily_return / benchmark_std_daily_return if benchmark_std_daily_return != 0 else 0
    #benchmark_annualized_sharpe_ratio = benchmark_daily_sharpe_ratio * np.sqrt(trading_days_per_year)
    #benchmark_annualized_return = benchmark_daily_return * trading_days_per_year
    #benchmark_annualized_volatility = benchmark_std_daily_return * np.sqrt(trading_days_per_year)
    
    return [
        ['Total years', f"{total_years:.2f}"],
        ['Total trading days', f"{total_days}"],
        ['Days w/ positive returns', f"{positive_returns}"],
        ['Days w/ negative returns', f"{negative_returns}"],
        ['Largest positive return (bps)', f"{max_return:.4f}"],
        ['Largest negative return (bps)', f"{min_return:.4f}"],
        ['Average Daily Return (bps)', f"{average_daily_return:.6f}"],
        ['Annualized Sharpe Ratio', f"{annualized_sharpe_ratio:.4f}"],
        ['Annualized Return (bps)', f"{annualized_return:.4f}"],
        ['Annualized Volatility (bps)', f"{annualized_volatility:.4f}"],
        
        #['Benchmark Annualized Sharpe Ratio', f"{benchmark_annualized_sharpe_ratio:.4f}"],
        #['Benchmark Annualized Return (bps)', f"{benchmark_annualized_return:.4f}"],
        #['Benchmark Annualized Volatility (bps)', f"{benchmark_annualized_volatility:.4f}"]
    ]

def create_table(ax, data, title):
    ax.axis('off')
    table = ax.table(cellText=data, loc='center', cellLoc='left')
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    
    col_widths = [0.5, 0.3]
    for (row, col), cell in table.get_celld().items():
        cell.set_text_props(fontproperties=prop)
        cell.set_width(col_widths[col])
    
    table.scale(1, 1.5)
    ax.set_title(title, fontproperties=prop, fontsize=14)

fig = plt.figure(figsize=(25, 10))
gs = fig.add_gridspec(2, 2, height_ratios=[1, 1], width_ratios=[2, 1])

ax1 = fig.add_subplot(gs[0, 0])
table_ax1 = fig.add_subplot(gs[0, 1])
ax2 = fig.add_subplot(gs[1, 0])
table_ax2 = fig.add_subplot(gs[1, 1])

create_plot(df, ax1, pd.Timestamp('2022-05-01'), pd.Timestamp('2023-05-31'), 'Bread Capital Daily Returns (May 2022 - May 2023)')
create_plot(df, ax2, pd.Timestamp('2023-06-01'), pd.Timestamp('2024-05-31'), 'Bread Capital Daily Returns (June 2023 - May 2024)')

table_data1 = calculate_stats(df, pd.Timestamp('2022-05-01'), pd.Timestamp('2023-05-31'))
table_data2 = calculate_stats(df, pd.Timestamp('2023-06-01'), pd.Timestamp('2024-05-31'))

create_table(table_ax1, table_data1, 'Statistics (May 2022 - May 2023)')
create_table(table_ax2, table_data2, 'Statistics (June 2023 - May 2024)')

plt.tight_layout()
plt.show()
