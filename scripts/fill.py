# Basic Fill the Tbale Information
def fillInfo(work_sheet,tem,this_month, last_month):
    tem['A3'].value = this_month

    tem['C5'].value = f"{this_month} OOS Rate"
    tem['E5'].value = f"{this_month} 7-Day Utilization"
    tem['G5'].value = f"{this_month} 5-Day Utilization"
    tem['C9'].value = f"{this_month} Miles Driven"
    tem['E9'].value = f"{this_month} Fobbed-In %"

    tem['F46'].value = f"{this_month} Weekday Utilization"
    tem['I46'].value = f"{this_month} Fobbed-In Percentage"


    #Last month information
    tem['C6'].value = f"{last_month} OOS Rate"
    tem['E6'].value = f"{last_month} 7-Day Utilization"
    tem['G6'].value = f"{last_month} 5-Day Utilization"
    tem['C10'].value = f"{last_month} Miles Driven"
    tem['E10'].value = f"{last_month} Fobbed-In %"

    tem['F14'].value = f"% change from {last_month}"
    tem['I14'].value = f"% change from {last_month}"

    tem['K14'].value = f"{last_month} Weekday Utilization"
    tem['M14'].value = f"{last_month} Fobbed-In Percentage"

    tem['E46'].value = f"{last_month} Weekday Utilization"
    tem['H46'].value = f"{last_month} Fobbed-In Percentage"

    #Fill in the last month total data
    tem['D6'].value = work_sheet['D5'].value
    tem['F6'].value = work_sheet['F5'].value
    tem['H6'].value = work_sheet['H5'].value
    tem['D10'].value = work_sheet['D9'].value
    tem['F10'].value = work_sheet['F9'].value

    #Fill in the last agency data
    tem['K16'] = work_sheet['H5'].value
    tem['M16'] = work_sheet['F9'].value
    total_weekday_utilization = 0
    total_Fobbed_In = 0
    for work_col,tem_col in zip(work_sheet.iter_rows(min_row=18,max_row=22),tem.iter_rows(min_row=18,max_row=22)):
        tem_col[10].value = work_col[4].value
        tem_col[12].value = work_col[7].value
        total_weekday_utilization += work_col[4].value
        total_Fobbed_In += work_col[7].value

    #Fill in the average data
    tem['K23'].value = total_weekday_utilization / 5
    tem['M23'].value = total_Fobbed_In / 5

    #Fill in the another division data
    for work_col,tem_col in zip(work_sheet.iter_rows(min_row=25,max_row=39),tem.iter_rows(min_row=25,max_row=39)):
        tem_col[10].value = work_col[4].value
        tem_col[12].value = work_col[7].value

    #Fill in the last month vehicle data
    total_lastmonth_utilization = 0
    total_lastmonth_FobbedIn = 0
    i = 1
    for work_col,tem_col in zip(work_sheet.iter_rows(min_row=49,max_row=57),tem.iter_rows(min_row=49,max_row=57)):
        tem_col[4].value = work_col[5].value
        tem_col[7].value = work_col[8].value
        if i <= 5: 
            total_lastmonth_utilization += work_col[5].value
            total_lastmonth_FobbedIn += work_col[8].value
        i+=1
    
    tem['E48'].value = total_lastmonth_utilization / 5
    tem['H48'].value = total_lastmonth_FobbedIn / 5

    return tem



# Fill the key data after calculation
def fillDivision(tem, final_table, Total_OOS, Total_7DayUtilization, Total_WeekdayUtilization, Total_MilesDriven, Total_FobbedIn, final_result_Division_vehicle, final_result_vehicle):
    #Fill the total Part
    tem['D5'].value = Total_OOS
    tem['F5'].value = Total_7DayUtilization
    tem['H5'].value = Total_WeekdayUtilization
    tem['D9'].value = Total_MilesDriven
    tem['F9'].value = Total_FobbedIn

    #Fill the division part
    for row in tem.iter_rows(min_row=18,max_row=22):
        for i in final_table.iterrows():
            if i[0] == row[1].value.strip():
                row[2].value = final_table.loc[i[0]]['OOS Rate']
                row[3].value = final_table.loc[i[0]]['7-Day Utilization']
                row[4].value = final_table.loc[i[0]]['Weekday Utilization']
                row[6].value = final_table.loc[i[0]]['Total Miles Driven']
                row[7].value = final_table.loc[i[0]]['Fobbed-In Percentage']
                break

    for row in tem.iter_rows(min_row=25,max_row=39):
        for i in final_table.iterrows():
            if i[0] == row[1].value:
                row[2].value = final_table.loc[i[0]]['OOS Rate']
                row[3].value = final_table.loc[i[0]]['7-Day Utilization']
                row[4].value = final_table.loc[i[0]]['Weekday Utilization']
                row[6].value = final_table.loc[i[0]]['Total Miles Driven']
                row[7].value = final_table.loc[i[0]]['Fobbed-In Percentage']
                break

    #Fill the vehicle part
    for row,i in zip(tem.iter_rows(min_row=49,max_row=53),range(len(final_result_Division_vehicle))):
        row[5].value = final_result_Division_vehicle.iloc[i]['Weekday Utilization Rate'] / 100
        row[8].value = final_result_Division_vehicle.iloc[i]['Fobbed In %'] / 100

    for row,i in zip(tem.iter_rows(min_row=54,max_row=59),range(len(final_result_vehicle))):
        row[5].value = final_result_vehicle.iloc[i]['Weekday Utilization Rate'] / 100
        row[8].value = final_result_vehicle.iloc[i]['Fobbed In %'] / 100

    return tem


