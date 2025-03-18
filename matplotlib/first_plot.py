
year = [1999,2000,2001,2002,2003,2004]
pop = [10000,11000,12000,13000,14000,15000]

# Print the last item from year and pop
print(year[-1])
print(pop[-1])

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Make a line plot: year on the x-axis, pop on the y-axis
plt.scatter(year,pop)

# Display the plot with plt.show()
plt.show()