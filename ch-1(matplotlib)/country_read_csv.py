import pandas as pd
import os 
import matplotlib.pyplot as plt
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
#path to csv file
csv_path = os.path.join(parent_dir,'country_data.csv')
# form .. import country_data as file
# df = pd.read_csv('../country_data.csv') #this import only when running the script form the same directly as it is relative improt
df = pd.read_csv(csv_path)
df_cleaned = df.dropna()
# print(df.head())
gdp_cap = df_cleaned['gdp_per_capita'].tolist() #convert any column of df to lis
pop = df_cleaned['population'].tolist()
life_exp_male = df_cleaned['life_expectancy_male'].tolist()

# data_dict = df.to_dict(orient= 'list')  convert the df into dict with header as key and all the column values as values
#Alternative:: orient = 'records' converts df into list of dictionaries with header/column name as key
# print(data_dict)
# print(df.iloc[:,0:5])   index based slicing of df  other are .loc and list of columns df[['c1','c2','c3']]
# life_exp = df['']
# print(gdp_cap[0:10],life_exp_male[0:10])
if __name__ == '__main__':
    print(df_cleaned.columns)
    plt.scatter(gdp_cap[0:100],life_exp_male[0:100])    #only used 3 points because data cleaning is not done
    plt.xscale('log')
    plt.show()