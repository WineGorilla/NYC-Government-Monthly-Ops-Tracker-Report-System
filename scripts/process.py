import pandas as pd
from scripts.utils import clean_value

def processData(route):
    test = pd.read_excel(route)
    test['Division/Boro'] = test['Division/Boro'].ffill()

    test['OOS Rate '] = test['OOS Rate '].apply(clean_value)
    test['Utilization Rate '] = test['Utilization Rate '].apply(clean_value)
    test['Weekday Utilization Rate '] = test['Weekday Utilization Rate '].apply(clean_value)
    test['Fobbed In % '] = test['Fobbed In % '].apply(clean_value)
    test['TotalMiles'] = test['TotalMiles'].apply(clean_value)
    return test