
# 以 平安银行 (000001.SZA) 的股票数据为例
df = D.history_data('000001.SZA', start_date='2015-01-01', end_date='2017-02-01',
                    fields=['open', 'high', 'low', 'close', 'adjust_factor', 'amount'])

# 日收益
df['return_1'] = df['close'] / df['close'].shift(1) - 1
# 5日收益
df['return_5'] = df['close'] / df['close'].shift(5) - 1

# 历史数据默认为后复权价格，除以 adjust_factor 得到实际价格
df['open'] /= df['adjust_factor']
df['high'] /= df['adjust_factor']
df['low'] /= df['adjust_factor']
df['close'] /= df['adjust_factor']

# 设置 date 为index，index将被用作x轴
df.set_index('date', inplace=True)
# 设置index的名字为None，在x轴将不显示x轴数据的名字
df.index.name = None