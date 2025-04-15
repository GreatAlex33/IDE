import numpy as np
from xml.etree.ElementInclude import include
from IPython.display import display
import pandas as pd
from regex import D

mask1 = melb_data['Type'] == 'townhouse'
mask2 = melb_data['Rooms'] > 2
melb_data[mask1 & mask2].sort_values(
    by=['Rooms', 'MeanRoomsSquare'],
    ascending=[True, False],
    ignore_index=True)
display(melb_data.loc[18])