# Programming and Scripting Project - Fisher’s Iris data set
# Maciej Burel - Advance approach

# This program runs trough other graphical representation methods on Iris dataset and diffrent techniques including tools like seaborn. 

# Import all necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Import libraries for scikit-learn for Machine Learning
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
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

# Transform data in dataset using Pandas Melt and create dataset_melt to be displayed in a meaningful way in swarmplot
dataset_melt = pd.melt(dataset, "species", var_name="measurement")
# Display swarmplot using dataset_melt data
sns.swarmplot(x="measurement", y="value", hue="species",palette="husl", data=dataset_melt)
plt.show()

# Machine Learning part of code

# Split the loaded dataset
array = dataset.values
X = array[:,0:4]
Y = array[:,4]
# Use 20% of data as validation dataset 
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

# Make predictions on validation dataset
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
predictions = knn.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions)) 
# Test prediction model by entering Iris sepal and petal user values
s_len = float(input("Please enter a sepal length in cm: "))
s_wid = float(input("Please enter a sepal width in cm: "))
p_len = float(input("Please enter a petal length in cm: "))
p_wid = float(input("Please enter a petal width in cm: "))
result = knn.predict([[s_len,s_wid,p_len,p_wid]])
print("\n")
print("The tested species is: ", result)



# https://machinelearningmastery.com/machine-learning-in-python-step-by-step/