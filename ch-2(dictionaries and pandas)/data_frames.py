# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd 

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

if __name__ == '__main__':
  
   # Definition of row_labels
    row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

    # Specify row labels of cars
    cars.index = row_labels
    # Print cars
    print(cars)   #columsn of cars can be of different datatypes which is not possible in numpy arrays

    # cars = pd.read_csv('cars.csv', index_col = 0)  index_col = 0 set so that the headers of columns of the dataframe donot confuse the first null element i.e. ,col1,col2 and unnammed =0

    # Print out cars
    print(cars)
   