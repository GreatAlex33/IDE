from re import X
from xml.etree.ElementInclude import include
from IPython.display import display
import pandas as pd
from regex import D

melb_data = pd.read_csv('data/melb_data_fe.csv', sep=',')


#Преобразуйте столбец Date в формат datetime и выделите квартал (quarter) продажи объектов недвижимости. 
#Найдите второй по популярности квартал продажи. В качестве ответа запишите число объектов, проданных в этом квартале.

#melb_data.info()

#nuniqcol = melb_data.apply(lambda x: x.nunique() < 150)
#for x in melb_data:
    #foreighn_lst = ['Date', 'Rooms', 'Bedroom', 'Bathroom', 'Car']
    #if nuniqcol[x] == True and x not in foreighn_lst:
       # melb_data[x] = melb_data[x].astype('category')
    #else:
        #pass

#melb_data.sort_values(by='AreaRatio', ascending=False, ignore_index=True)

#Какая риелторская компания (SellerG) имеет наименьшую общую выручку за период с 1 мая по 1 сентября (включительно) 2017 года?
#Для ответа на этот вопрос рассчитайте сумму продаж (Price) каждой компании в заданный период.
#Не забудьте перевести даты в формат datetime.

melb_data['Date'] = pd.to_datetime(melb_data['Date'])

date1 = pd.to_datetime('2017-05-01')
date2 = pd.to_datetime('2017-09-01')
mask = (date1 <= melb_data['Date']) & (melb_data['Date']<= date2)
display(melb_data[mask].groupby('SellerG')['Price'].sum().sort_values(ascending=True))