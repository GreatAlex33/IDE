from email.utils import parsedate_to_datetime
from re import X
from xml.etree.ElementInclude import include
from IPython.display import display
import pandas as pd
from regex import D

ratio1 = pd.read_csv('data/ratings1.csv', sep=',')
ratio2 = pd.read_csv('data/ratings2.csv', sep=',')
dates = pd.read_csv('data/dates.csv', sep=',')
movies = pd.read_csv('data/movies.csv', sep=',')

pd.to_datetime(dates['date']).dt.year.value_counts()
ratings = pd.concat([ratio1, ratio2],ignore_index=True)
ratings = ratings.drop_duplicates(ignore_index=True)
ratings_dates = pd.concat([ratings, dates], axis=1)
joined_false = ratings_dates.join(
    movies,
    rsuffix='_right',
    how='left'
)
joined = ratings_dates.join(
    movies.set_index('movieId'),
    on='movieId',
    how='left'
)
display(joined.head())