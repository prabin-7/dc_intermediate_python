# Import cars data
import pandas as pd
import os
import sys

# parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
#path to csv file
dir_file = os.path.abspath(os.path.dirname(__file__))  #gives the abs path of the file running currently
csv_path = os.path.join(dir_file,'cars.csv')           #adds the file name to the location so that python can search for the exact file


cars = pd.read_csv(csv_path, index_col = 0)

# Print out country column as Pandas Series
print(cars['country'])


# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country','drives_right']])


# Print out first 3 observations
print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])


#exercise -3:
# Print out observation for Japan as  a serires using single bracket with df.loc
print(cars.loc['JPN'])

# Print out observations for Australia and Egypt
print(cars.loc[['AUS','EG']])

#exercise-4
# Print out drives_right value of Morocco
print(cars.loc[['MOR'],['drives_right']])

# Print sub-DataFrame
print(cars.loc[['RU','MOR'],['country','drives_right']])


# exercise-5?
# Print out drives_right column as Series
print(cars.loc[:,'drives_right'])

# Print out drives_right column as DataFrame
print(cars.loc[:,['drives_right']])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:,['cars_per_cap','drives_right']])