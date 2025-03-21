import pandas as pd 
import numpy as np
import os 

parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
csv_path = os.path.join(parent_path,'ch-2(dictionaries and pandas)/cars.csv')

cars = pd.read_csv(csv_path, index_col = 0)
# print(cars)

# for lab, row in cars.iterrows():
#     print(lab)             #prints the label
#     print()
#     print(row)             #prints a pandas series of all the row elements 


#using list:
# upper_case = []
# for lab,row in cars.iterrows():
#     upper_case.append(row['country'].upper())

# cars['COUNTRY'] = upper_case          #dictionary ma add garae jastai raixa yo to add new element in dataframes


# #using normal loop 
# for lab, row in cars.iterrows() :
#     cars.loc[lab, "COUNTRY"] = row["country"].upper()

#using one liner .apply method 

cars['COUNTRY'] =   cars['country'].apply(str.upper)


print(cars)