import matplotlib.pyplot as plt 
from country_read_csv import gdp_cap,life_exp_male,pop

plt.figure()
plt.hist(life_exp_male)
plt.title('histogram with 10 bins')
# plt.show()  #use it at last to display all the folders
# plt.clf()   # cleans it up so you can start fresh

plt.figure()
plt.hist(life_exp_male, bins = 5)
plt.title('histogram with 5 bins')
plt.show()