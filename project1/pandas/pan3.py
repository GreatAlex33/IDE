from xml.etree.ElementInclude import include
from IPython.display import display
import pandas as pd
from regex import D
data = pd.read_csv('data/citibike-tripdata.csv', sep=',')

data['Age'] = data['birth year'].apply(lambda x: 2018 - x)
data = data.drop(['birth year'], axis=1)
#data['starttime'] = pd.to_datetime(data['starttime']).dt.minute
#data['stoptime'] = pd.to_datetime(data['stoptime']).dt.minute
#data['trip duration'] = data['stoptime'] - data['starttime']
data['starttime'] = pd.to_datetime(data['starttime']).dt.day_of_week
def weekofbike(dat):
    if dat >= 5:
        return 1
    else:
        return 0
data['weekend'] = data['starttime'].apply(weekofbike)
data['weekend'].value_counts()