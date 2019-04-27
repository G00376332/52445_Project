# Programming and Scripting Project - Fisher’s Iris data set
# Maciej Burel - Final Project
# Main Program - Basic work on dataset

# Import os to issue operating system terminal commnads
import os
# Import timer to use in time sleep
import time
# Use pandas to work on data analysis and create useful outputs.
import pandas
# Import colour map
import matplotlib.cm as cm
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
# Clear Python terminal windows. Check OS before issue a command.
if os.name =="nt":
    cl = "cls"
else:
    cl = "clear"

os.system(cl)
print("Welcome to Programing and Scripting Project Program about the Iris Data Set.")
print("This program contains the Iris data set which was automatically loaded into the program.")
print("You can choose from the following menu option to display basic information and plot different graphs.\n")

# Creating simple menu for user choice
def menu():       
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Display information about row and columns in data set")
    print("2. Display first 10 rows of segregated data")
    print("3. Display the statistical summary")
    print("4. Display box and whisker plots")
    print("5. Display histogram of each input variable")
    print("6. Display scatter matrix plot")
    print("7. Exit")
    print(66 * "-")
# Setting variable "cond" equal "True"   
cond=True      
# Using while loop until "cond = False"  
while cond:
    # Display menu
    menu()    
    
    choice = input("Enter your selection [1-7]: ")

    if (choice.isdigit()):
        n = int(choice)
        if n==1:     
            # Segregate data and display basic information about rows and columns.
            print("\n")
            print("Rows, Columns")
            print(dataset.shape)
            print("\n")
            input("Press Enter to continue...")
            os.system(cl)
        elif n==2:
            # Display first 10 rows of data.
            print("\n")
            print(dataset.head(10))
            print("\n")
            input("Press Enter to continue...")
            os.system(cl)
        elif n==3:
            # Display the statistical summary of each attribute: count, mean, min and max values and percentiles. 
            print("\n")
            print(dataset.describe())
            print("\n")
            input("Press Enter to continue...")
            os.system(cl)
        elif n==4:
            # Present data in plot. Using box and whisker plots.
            dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
            plt.show()
            os.system(cl)
        elif n==5:
            # Present data as histogram of each input variable.
            dataset.hist()
            plt.show()
            os.system(cl)
        elif n==6:
            # Display scatter matrix plot
            # Assign different colours for different class            
            cmap = {"Iris-setosa": "red", "Iris-versicolor": "green", "Iris-virginica": "blue"} 
            scatter_matrix(dataset, c=[cmap[col] for col in dataset["class"]])
            plt.show()
            os.system(cl)
        elif n==7:
            # This will make the while loop to end 
            os.system(cl)
            print("Thank you for using this program :)\nGoodbye!")
            # Wait for displaying a message for 2s
            time.sleep(2)
            cond=False     
            os.system(cl)          
        else:
            print("Wrong selection. Enter any key to continue..")
            input()
            os.system(cl)
    else:
        # Any integer inputs other than values 1-5 we print an error message
        print("Wrong selection. Enter any key to continue..")
        input()
        os.system(cl)




