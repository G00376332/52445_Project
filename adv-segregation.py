# Programming and Scripting Project - Fisher’s Iris data set
# Maciej Burel - Advance approach

# This program runs trough other graphical representation methods on Iris dataset and diffrent techniques including tools like seaborn. 

# Import all necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load Iris data from seaborn database
dataset = sns.load_dataset("iris")

# Like in basic segregation.py program display basic set of information about dataset.

print(dataset.head())
print(dataset.shape)
print(dataset.describe())

# Display pairplot graph. Set different than default colours and markers
sns.pairplot(dataset, hue="species", palette="husl", markers=["o", "s", "D"])
plt.show()
# Show violin plots based on multiple species features
sns.violinplot(x="species", y="petal_width", palette="husl", data=dataset)
plt.show()
sns.violinplot(x="species", y="petal_length", palette="husl", data=dataset)
plt.show()
sns.violinplot(x="species", y="sepal_width", palette="husl", data=dataset)
plt.show()
sns.violinplot(x="species", y="sepal_length", palette="husl", data=dataset)
plt.show()

# "Melt" the dataset
#dataset_melt = pd.melt(dataset, "species", var_name="measurement")
# Draw a categorical scatterplot
sns.swarmplot(x="measurement", y="value", hue="species",palette="husl", data=dataset)
plt.show()



