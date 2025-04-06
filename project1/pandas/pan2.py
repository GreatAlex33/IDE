from IPython.display import display
import pandas as pd
ufo_data = pd.read_csv('data/ufo.csv', sep=',')

ufo_data['Time'] = pd.to_datetime(ufo_data['Time'], dayfirst=True,format='mixed')

years_sold = ufo_data['Time'].dt.year
print(years_sold.mode()[0])