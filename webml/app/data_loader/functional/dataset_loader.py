'''
Interacts with the visual compoment DatasetLoader
Contains methods on auto-detecting columns
'''
import pandas as pd
from typing import Dict, List
from webml.constants import DTYPE_NUMERICAL, DTYPE_CATEGORICAL

class DatasetLoaderFunc:
    def __init__(self,df : pd.DataFrame) -> None:
        self.df = df
        pass

    def parse_columns(self,auto : bool=True,mapping: Dict[str,List[str]]=None):
        '''
        parses its own columns into appropriate format.
        auto-detects numerical as numerical, categorical as categorical
        '''
        if mapping is not None:
            mapping['numerical']
