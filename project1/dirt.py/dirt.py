import numpy as np
from xml.etree.ElementInclude import include
from IPython.display import display
import pandas as pd
from regex import D

def concat_user_files(path):
    result = pd.DataFrame()
    files = os.listdir(path)
    files = files.sort()
    for x in files:
        openfile = pd.read_csv(path + '/' + x)
        result = pd.concat([result, openfile], axis=0, ignore_index=True)
    result = result.drop_duplicates()
    return result