# Import numpy as np
import numpy as np
import matplotlib.pyplot as plt
from country_read_csv import gdp_cap,life_exp_male as life_exp, pop 
# Store pop as a numpy array: np_pop
np_pop = np.array(pop)

# Double np_pop
np_pop = np_pop //10000

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2024')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()


'''future enhancements to the plot to Improve the Plot

Scale the Population Data: Divide the population values by a large number (e.g., 1 million) to get reasonable marker sizes.
Add Transparency: Use the alpha parameter in plt.scatter() to add transparency to the markers, especially if there is significant overlap.
Add a Legend: Include a legend that explains the size scaling of the markers.
Consider Color Mapping: If you have additional data (e.g., continent), consider using color to represent that information.'''

# plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2, c = col, alpha = 0.8)