from xml.etree.ElementInclude import include
from IPython.display import display
import pandas as pd

melb_data = pd.read_csv('data/melb_data.csv', sep=',')

melb_data = melb_data.fillna(value=0)
melb_data['Car'] = melb_data['Car'].astype('int64')
melb_data['Bedroom'] = melb_data['Bedroom'].astype('int64')
melb_data['Bathroom'] = melb_data['Bathroom'].astype('int64')
melb_data['Propertycount'] = melb_data['Propertycount'].astype('int64')
melb_data['YearBuilt'] = melb_data['YearBuilt'].astype('int64')

med_building = melb_data['BuildingArea'].median()
mid_building = melb_data['BuildingArea'].mean()
mask = melb_data['Price'] > 2000000
melb_data[mask].head()
melb_data[melb_data['Rooms'] == 3].shape[0]
melb_data[(melb_data['Rooms'] == 3) & (melb_data['Price'] < 300000)].shape[0]
melb_data[((melb_data['Rooms'] == 3) | (melb_data['BuildingArea'] > 100)) & (melb_data['Price'] < 300000)].shape[0]
melb_data[melb_data['Type'] == 't']['Rooms'].max()
mean_price = melb_data['Price'].mean()
melb_data[melb_data['Price'] > mean_price]['BuildingArea'].median()
#Задание 8.4
melb_data[((melb_data['YearBuilt'] > 2015) | (melb_data['Rooms'] > 5)) & (melb_data['Price'] < 1000000)]['Price'].mean()
#Задание 8.5
melb_data[(melb_data['Type'] == 'h') & (melb_data['Price'] < 3000000)] ['Regionname'].value_counts()
melb_df = melb_data.copy()
melb_df = melb_df.drop(['index', 'Coordinates'], axis=1)
total_rooms = melb_df['Rooms'] + melb_df['Bedroom'] + melb_df['Bathroom']
melb_df['MeanRoomsArea'] = melb_df['BuildingArea'] / total_rooms
diff_area = melb_df['BuildingArea'] - melb_df['Landsize']
sum_area = melb_df['BuildingArea'] + melb_df['Landsize']
melb_df['AreaRatio'] = diff_area/sum_area
melb_df['Date'] = pd.to_datetime(melb_df['Date'], dayfirst=True,format='mixed')
years_sold = melb_df['Date'].dt.year

'Min year sold:', years_sold.min()
'Max year sold:', years_sold.max()
'Mode year sold:', years_sold.mode()[0]

melb_df['MonthSale'] = melb_df['Date'].dt.month
melb_df['MonthSale'].value_counts(normalize=True)
delta_days = melb_df['Date'] - pd.to_datetime('2016-01-01') 
melb_df['AgeBuilding'] = melb_df['Date'].dt.year - melb_df['YearBuilt']
melb_df = melb_df.drop('YearBuilt', axis=1)
melb_df['WeekdaySale'] = melb_df['Date'].dt.day_of_week
display((melb_df['WeekdaySale'] >= 5).value_counts())