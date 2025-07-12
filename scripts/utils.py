import numpy as np
import pandas as pd
from scripts.constants import No_dict 

def clean_value(x):
    if pd.isna(x):
        return np.nan

    if isinstance(x,str):
        x_clean = x.strip().replace(',','')
        if x_clean.upper() in No_dict:
            return np.nan
        if x_clean.endswith('%'):
            try:
                return float(x_clean.rstrip('%'))
            except ValueError:
                return np.nan
        try:
            return float(x_clean)
        except ValueError:
            return np.nan

    if isinstance(x,(int,float)):
        return float(x)
    return np.nan
