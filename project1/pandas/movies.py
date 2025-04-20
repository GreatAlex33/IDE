from email.utils import parsedate_to_datetime
from re import X
from xml.etree.ElementInclude import include
from IPython.display import display
from numpy import outer
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


items_df = pd.DataFrame({
            'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 100132, 312394],
            'vendor': ['Samsung', 'LG', 'Apple', 'Apple', 'LG', 'Apple', 'Samsung', 'Samsung', 'LG', 'ZTE'],
            'stock_count': [54, 33, 122, 18, 102, 43, 77, 143, 60, 19]
        })

purchase_df = pd.DataFrame({
            'purchase_id': [101, 101, 101, 112, 121, 145, 145, 145, 145, 221],
            'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 103845, 100132],
            'price': [13900, 5330, 38200, 49990, 9890, 33000, 67500, 34500, 89900, 114]
            })

merged = items_df.merge(purchase_df,
                        on='item_id',
                        how='inner')
merged['Total'] = merged['stock_count'] * merged['price']
income = merged['Total'].sum()
merged = merged.drop(['Total'], axis=1)
display(merged)