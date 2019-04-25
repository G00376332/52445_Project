# Programming and Scripting Project - Fisher’s Iris data set
# Maciej Burel - Final Project

# Use pandas to work on data analysis and create useful outputs.
import pandas
# Use matplotlib to plot and visualize data.
import matplotlib.pyplot as plt
# Import scatter matrix plot from pandas
from pandas.plotting import scatter_matrix
# Load dataset "iris.data" from the folder Dataset. 
data = 'Dataset/iris.data'
# Assign appropriete column names.
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
# Use pandas to read file as CSV format. Separate column using coma as delimiter.
dataset = pandas.read_csv(data, names=names)
# Segregate data and display basic information about row and columns.
print(dataset.shape)
# Dsiplay first 10 rows of data.
print(dataset.head(10))
# Display the statistical summary of each attribute: count, mean, min and max values and percentiles. 
print(dataset.describe())
# Present data in plot. Using box and whisker plots.
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()
# Present data as histogram of each input variable.
dataset.hist()
plt.show()
# Display scatter matrix plot
scatter_matrix(dataset)
plt.show()