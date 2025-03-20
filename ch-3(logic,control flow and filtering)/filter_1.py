# Import cars data
import pandas as pd
import os 

'''reading a csv from sibling folderes can be done by using the os module
- first find the abspath of the dir of the __file__ then parent dir by  joining to '..'
- then add the relative path of the csv file  '''
path1 = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
csv_path = os.path.join(path1,'ch-2(dictionaries and pandas)','cars.csv')
# path2 = os.path.join(path1,)
cars = pd.read_csv(csv_path, index_col = 0)

# Extract drives_right column as Series: dr
# dr = cars['drives_right']

#withour using the intermediate variable dr:
sel = cars[cars['drives_right']]



# Use dr to subset cars: sel
# sel = cars[dr]

# Print sel
print(sel,"\n")

# exercise 3
car_maniac = cars[cars['cars_per_cap']>500]
print(car_maniac)