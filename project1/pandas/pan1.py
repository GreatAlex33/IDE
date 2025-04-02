from IPython.display import display
import pandas as pd
melb_data = pd.read_csv('data/melb_data.csv', sep=',')

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
display(melb_data[(melb_data['Type'] == 'h') & (melb_data['Price'] < 3000000)] ['Regionname'].value_counts())