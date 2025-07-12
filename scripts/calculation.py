import pandas as pd
from scripts.constants import *

def divisionCalculate(test):
    result_groupby = test.groupby("Division/Boro").agg({'OOS Rate ':'mean','Utilization Rate ':'mean','Weekday Utilization Rate ':'mean','TotalMiles':'mean','Fobbed In % ':'mean'})

    final_table = pd.DataFrame()
    for i in result_groupby.index:
        if Division_dict.get(i):
            new_index = Division_dict.get(i)
            new_row = pd.DataFrame({
                'OOS Rate':result_groupby.loc[i,'OOS Rate '],
                '7-Day Utilization':result_groupby.loc[i,'Utilization Rate '],
                'Weekday Utilization':result_groupby.loc[i,'Weekday Utilization Rate '],
                'Total Miles Driven':result_groupby.loc[i,'TotalMiles'],
                'Fobbed-In Percentage':result_groupby.loc[i,'Fobbed In % ']
            },index=[new_index])
            final_table = pd.concat([final_table,new_row])

    Total_OOS = (final_table.loc['BX']['OOS Rate'] + final_table.loc['BK']['OOS Rate'] + final_table.loc['MN']['OOS Rate'] + final_table.loc['QN']['OOS Rate'] + final_table.loc['SI']['OOS Rate']) / 5

    Total_7DayUtilization = (final_table.loc['BX']['7-Day Utilization'] + final_table.loc['BK']['7-Day Utilization'] + final_table.loc['MN']['7-Day Utilization'] + final_table.loc['QN']['7-Day Utilization'] + final_table.loc['SI']['7-Day Utilization']) / 5

    Total_WeekdayUtilization = (final_table.loc['BX']['Weekday Utilization'] + final_table.loc['BK']['Weekday Utilization'] + final_table.loc['MN']['Weekday Utilization'] + final_table.loc['QN']['Weekday Utilization'] + final_table.loc['SI']['Weekday Utilization']) / 5

    Total_MilesDriven = (final_table.loc['BX']['Total Miles Driven'] + final_table.loc['BK']['Total Miles Driven'] + final_table.loc['MN']['Total Miles Driven'] + final_table.loc['QN']['Total Miles Driven'] + final_table.loc['SI']['Total Miles Driven']) / 5

    Total_FobbedIn = (final_table.loc['BX']['Fobbed-In Percentage'] + final_table.loc['BK']['Fobbed-In Percentage'] + final_table.loc['MN']['Fobbed-In Percentage'] + final_table.loc['QN']['Fobbed-In Percentage'] + final_table.loc['SI']['Fobbed-In Percentage']) / 5
            
    return final_table, Total_OOS, Total_7DayUtilization, Total_WeekdayUtilization, Total_MilesDriven, Total_FobbedIn


def vehicleCalculate(test):
    Total_Group = test.groupby("Type").agg({'Weekday Utilization Rate ':'mean','Fobbed In % ':'mean'})
    Division_Group = test.groupby(["Division/Boro","Type"]).agg({'Weekday Utilization Rate ':'mean','Fobbed In % ':'mean'})
    
    BK = BX = MN = QN = SI = [0,0]

    for i in Division_Group.index:
        if (i[0] == 'DPAR-BROOKLYN'):
            if (i[1] in pickups_features):
                BK += Division_Group.loc[i[0],i[1]].values
                
        if (i[0] == 'DPAR-BRONX'):
            if (i[1] in pickups_features):
                BX += Division_Group.loc[i[0],i[1]].values
                
        if (i[0] == 'DPAR-MANHATTAN'):
            if (i[1] in pickups_features):
                MN += Division_Group.loc[i[0],i[1]].values
                
        if (i[0] == 'DPAR-QUEENS'):
            if (i[1] in pickups_features):
                QN += Division_Group.loc[i[0],i[1]].values
                
        if (i[0] == 'DPAR-STATEN ISLAND'):
            if (i[1] in pickups_features):
                SI += Division_Group.loc[i[0],i[1]].values

    final_result_Division_vehicle = pd.DataFrame({
        'BX':BX,
        'BK':BK,
        'MN':MN,
        'QN':QN,
        'SI':SI
    },index=['Weekday Utilization Rate','Fobbed In %']).T

    packers_sum = sedans_sum = suvs_sum = vans_sum = [0,0]

    for i in Total_Group.index.values:   
        if i in sedans_features:
            sedans_sum += Total_Group.loc[f"{i}"].values
        elif i in suvs_features:
            suvs_sum += Total_Group.loc[f"{i}"].values
        elif i in vans_features:
            vans_sum += Total_Group.loc[f"{i}"].values
        elif i in packer_features:
            packers_sum += Total_Group.loc[f"{i}"].values

    final_result_vehicle = pd.DataFrame({
        'Packers':packers_sum,
        'Sedans':sedans_sum,
        'SUVs':suvs_sum,
        'Vans':vans_sum
    },index=['Weekday Utilization Rate','Fobbed In %']).T

    return final_result_Division_vehicle, final_result_vehicle

