from IPython.display import display
import pandas as pd
ufo_data = pd.read_csv('data/ufo.csv', sep=',')

ufo_data['Time'] = pd.to_datetime(ufo_data['Time'], dayfirst=True,format='mixed')

years_sold = ufo_data['Time'].dt.year
ufo_data['Date'] = pd.to_datetime(ufo_data['Time'])
delta = (ufo_data[ufo_data['State'] == 'NV']['Date'].diff())
display((delta.dt.days).mean())
