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
(melb_df['WeekdaySale'] >= 5).value_counts()


melb_df['Address'].nunique()
# На вход данной функции поступает строка с адресом.
def get_street_type(address):
# Создаём список географических пометок exclude_list.
    exclude_list = ['N', 'S', 'W', 'E']
# Метод split() разбивает строку на слова по пробелу.
# В результате получаем список слов в строке и заносим его в переменную address_list.
    address = str(address)
    address_list = address.split(' ')
# Обрезаем список, оставляя в нём только последний элемент,
# потенциальный подтип улицы, и заносим в переменную street_type.
    street_type = address_list[-1]
# Делаем проверку на то, что полученный подтип является географической пометкой.
# Для этого проверяем его на наличие в списке exclude_list.
    if street_type in exclude_list:
# Если переменная street_type является географической пометкой,
# переопределяем её на второй элемент с конца списка address_list.
        street_type = address_list[-2]
# Возвращаем переменную street_type, в которой хранится подтип улицы.
    return street_type
street_types = melb_df['Address'].apply(get_street_type)
popular_stypes =street_types.value_counts().nlargest(10).index
melb_df['StreetType'] = street_types.apply(lambda x: x if x in popular_stypes else 'other')
melb_df = melb_df.drop('Address', axis=1)

# Задание 4.2Ранее, в задании 3.3, мы создали признак WeekdaySale в таблице melb_df — день недели продажи. Из полученных в задании результатов можно сделать вывод, 
# что объекты недвижимости в Мельбурне продаются преимущественно по выходным (суббота и воскресенье).Напишите функцию get_weekend(weekday), 
# которая принимает на вход элемент столбца WeekdaySale и возвращает 1, если день является выходным, и 0 — в противном случае, и создайте столбец Weekend в таблице melb_df с помощью неё.
# Примените эту функцию к столбцу и вычислите среднюю цену объекта недвижимости, проданного в выходные дни. Результат округлите до целых

def get_weekend(weekday):
    if weekday >= 5:
        return 1
    else:
        return 0
new_col = melb_df['WeekdaySale'].apply(get_weekend)
melb_df['Weekend'] = new_col
melb_df[melb_df['Weekend'] == 1]['Price'].mean()

#melb_df = melb_df.drop(13580, axis=0)

popular_company = melb_df['SellerG'].value_counts().nlargest(49).index
melb_df['SellerG'] = melb_df['SellerG'].apply(lambda x: x if x in popular_company else 'other')
difference1 = (melb_df[melb_df['SellerG'] == 'Nelson']['Price'].min()) 
difference2 = (melb_df[melb_df['SellerG'] == 'other']['Price'].min())


cols_to_exclude = ['Date', 'Rooms', 'Bedroom', 'Bathroom', 'Car'] # список столбцов, которые мы не берём во внимание
max_unique_count = 150 # задаём максимальное число уникальных категорий
for col in melb_df.columns: # цикл по именам столбцов
    if melb_df[col].nunique() < max_unique_count and col not in cols_to_exclude: # проверяем условие
        melb_df[col] = melb_df[col].astype('category') # преобразуем тип столбца
#melb_df.info()

melb_df['Regionname'].cat.categories

melb_df['Type'] = melb_df['Type'].cat.rename_categories({
    'u': 'unit',
    't': 'townhouse',
    'h': 'house'
})
melb_df['Type']

display(melb_df.info())
popular_sub = melb_df['Suburb'].value_counts().nlargest(119).index
melb_df['Suburb'] = melb_df['Suburb'].apply(lambda x: x if x in popular_sub else 'other')
melb_df['Suburb'].astype('category')
display(melb_df.info())