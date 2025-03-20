import pandas as pd 
import numpy as np
import os 

parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
# csv_path = os.path.join(parent_path,'ch-2(dictionaries and pandas)','cars.csv')
csv_path = os.path.join(parent_path,'ch-2(dictionaries and pandas)/cars.csv')
# print(csv_path)

cars = pd.read_csv(csv_path, index_col=0)
# print(cars)

medium =  cars[np.logical_and(cars['cars_per_cap']>100,cars['cars_per_cap']<500)]
print(medium)