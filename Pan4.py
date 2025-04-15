from xml.etree.ElementInclude import include
from IPython.display import display
import pandas as pd
from regex import D

melb_data = pd.read_csv('data/melb_data_fe.csv', sep=',')


#Преобразуйте столбец Date в формат datetime и выделите квартал (quarter) продажи объектов недвижимости. 
#Найдите второй по популярности квартал продажи. В качестве ответа запишите число объектов, проданных в этом квартале.
melb_data['Date'] = pd.to_datetime(melb_data['Date']).dt.quarter
#melb_data.info()

#nuniqcol = melb_data.apply(lambda x: x.nunique() < 150)
#for x in melb_data:
    #foreighn_lst = ['Date', 'Rooms', 'Bedroom', 'Bathroom', 'Car']
    #if nuniqcol[x] == True and x not in foreighn_lst:
       # melb_data[x] = melb_data[x].astype('category')
    #else:
        #pass

#melb_data.sort_values(by='AreaRatio', ascending=False, ignore_index=True)



display(melb_data.groupby('Regionname')['Lattitude'].std().sort_values(ascending=False))