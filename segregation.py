# Programming and Scripting Project - Fisher’s Iris data set
# Maciej Burel - Final Project

# Use pandas to work on data analysis and create useful outputs.
import pandas

# Load dataset "iris.data" from the folder Dataset 
data = 'Dataset/iris.data'
# Assign appropriete column names
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
# Use pandas to read file as CSV format. Separate column using coma as delimiter.
dataset = pandas.read_csv(data, names=names)
# Segregate data and display basic information about row and columns 
print(dataset.shape)
# Dsiplay first 20 rows of data
print(dataset.head(20))
# Display the statistical summary of each attribute: count, mean, min and max values and percentiles. 
print(dataset.describe())
