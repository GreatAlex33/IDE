from re import X
from xml.etree.ElementInclude import include
from IPython.display import display
import pandas as pd
from regex import D

orders = pd.read_csv('data/orders.csv', sep=';')
products = pd.read_csv('data/products.csv', sep=';')
display(products)
display(orders)

