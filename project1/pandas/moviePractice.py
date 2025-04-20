from email.utils import parsedate_to_datetime
from re import X
from xml.etree.ElementInclude import include
from IPython.display import display
from numpy import outer
import pandas as pd
from regex import D
import re

ratings = pd.read_csv('data/ratings_movies.csv', sep=',')

def get_year_release(arg):
    #находим все слова по шаблону "(DDDD)"
    candidates = re.findall(r'\(\d{4}\)', arg) 
    # проверяем число вхождений
    if len(candidates) > 0:
        #если число вхождений больше 0,
	#очищаем строку от знаков "(" и ")"
        year = candidates[0].replace('(', '')
        year = year.replace(')', '')
        return int(year)
    else:
        #если год не указан, возвращаем None
        return None
ratings['year_release'] = ratings['title'].apply(get_year_release)

#mask = ratings['year_release'] == 1999
#ratings[mask].groupby('title')['rating'].mean().sort_values(ascending=True)

#mask1 = ratings['year_release'] == 2010
#ratings[mask1].groupby('genres')['rating'].mean().sort_values(ascending=True)

#ratings.groupby('userId')['genres'].nunique()
#display(ratings.groupby('userId')['genres'].nunique().sort_values(ascending=True))

#display(ratings.groupby('userId')['rating'].agg(['count','mean']).sort_values(by='count',ascending=True).head(20))

#mask2 = ratings['year_release'] == 2018
#modern = ratings[mask2].groupby('genres')['rating'].agg(['count','mean']).copy()

ratings['year_rating'] = pd.to_datetime(ratings['date']).dt.year
svod = ratings.pivot_table(
    values='rating',
    index='year_rating',
    columns='genres',
    aggfunc='mean'
)

