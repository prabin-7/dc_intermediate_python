from country_read_csv import gdp_cap,life_exp_male,pop
import matplotlib.pyplot as plt

#creation of plot
plt.scatter(gdp_cap,life_exp_male)

xlab = 'GDP per capita [in USD]'
ylab = 'life expectancy of males [in years]'
tick_val = [x for x in range(0,140000,10000)]
print(tick_val)
tick_label = [f'{x//1000}k' for x in range(0,140000,10000)]
# tick_label = ['1k', '10k', '10k','20k','30k','40k','50k','60k','70k','80k']
title = 'GDP PER CAPITA AND LIFE EXPECTANCY'

#customisation of plot
plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(title)
plt.xticks(tick_val, tick_label)

#show the plot
plt.show()