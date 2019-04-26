# Programming and Scripting Project - Fisher’s Iris data set

This repository contains the project about Fisher's Iris data set. It includes documentation and code in Python based on researches. 

[See here for the instructions](https://github.com/ianmcloughlin/project-pands/raw/master/project.pdf)

## The main goal and the key points

* Research background information about the data set and write a summary about it.
* Keep a list of references you used in completing the project.
* Download the data set and write some Python code to investigate it.
* Summarise the data set by, for example, calculating the maximum, minimum and mean of each column of the data set. Create Python script
* Write a summary of your investigations.
* Include supporting tables and graphics as you deem necessary.

## Background information and summary about the data set

Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper.The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis. It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. The data set consists of 50 samples from each of three species of Iris:

|![Iris Versicolor](Photos/Iris_Vesicolor.JPG)|![Iris Setosa](Photos/Iris_Setosa.JPG)|![Iris Virginica](Photos/Iris_Virginica.JPG)|
|-----------|-----------|-----------|
| <p align="center"> **Iris Versicolor** </p> | <p align="center"> **Iris Setosa** </p> | <p align="center"> **Iris Virginica** </p> |

Four features were measured from each sample:
* Sepal length(cm)
* Sepal Width(cm)
* Petal Length(cm)
* Petal Width(cm)

![Iris Description](Photos/Iris_description1.JPG)

Based on the combination of the above four features, Fisher developed a linear discriminant model to distinguish the species from each other. 
Interesting and challenging in the relation of Iris flowers is the fact that sepal and petal look quite similar contrary to other flowers where sepal is usually green and easy to distinguish from the petal.

![Sepal Petal](Photos/sepal_petal.JPG)

## Data set review

The data set used for this project was downloaded from the UCI Machine Learning Repository. This repository contains iris dataset widely used in many publications and research projects across the world. The Iris flower data set is a classic, well-known data set example for data mining and data exploration and is traditionally used for classification and prediction

* Number of Instances: 150 (50 in each of three classes)

* Number of Attributes: 4 numeric, predictive attributes and the class


Attribute Information:
1. sepal length in cm
1. sepal width in cm
1. petal length in cm
1. petal width in cm
1. class:
    
    * Iris Setosa
    * Iris Versicolour
    * Iris Virginica
    
Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other. This data set became a typical test case for many statistical classification techniques in machine learning.

## Investigating data set using Python script

### Evaluating data sets

The data set contains raw data with comma-separated values. To make those data more meaningful and readable for a regular user the Python script [segregation.py][1] has been created. The pandas was used to load and read file "iris.data" from local folder "Dataset". The names of each column were specified when loading the data. Having data loaded in to pandas it was easy to obtain the required information.

Using ***print(dataset.shape)*** it displays the number of instances and attributes: **(150, 5)**.

To visualize first ten rows data with appropriate column names ***print(dataset.head(10))*** was used.<br />
This displayed segregated data in the [terminal](Outputs/dataoutputs.png) as in the table below.

| No.| sepal-length | sepal-width | petal-length | petal-width | class |
|---|-----|-----|-----|-----|-------------|
| 0 | 5.1 | 3.5 | 1.4 | 0.2 | Iris-setosa |
| 1 | 4.9 | 3.0 | 1.4 | 0.2 | Iris-setosa |
| 2 | 4.7 | 3.2 | 1.3 | 0.2 | Iris-setosa |
| 3 | 4.6 | 3.1 | 1.5 | 0.2 | Iris-setosa |
| 4 | 5.0 | 3.6 | 1.4 | 0.2 | Iris-setosa |
| 5 | 5.4 | 3.9 | 1.7 | 0.4 | Iris-setosa |
| 6 | 4.6 | 3.4 | 1.4 | 0.3 | Iris-setosa |
| 7 | 5.0 | 3.4 | 1.5 | 0.2 | Iris-setosa |
| 8 | 4.4 | 2.9 | 1.4 | 0.2 | Iris-setosa |
| 9 | 4.9 | 3.1 | 1.5 | 0.1 | Iris-setosa |

Finally using ***print(dataset.describe())***, it was possible to do some statistical summary on data set.

| | sepal-length | sepal-width | petal-length | petal-width |
|---|-----|-----|-----|-----|
| **count** | 150.000000 | 150.000000 | 150.000000 | 150.000000 |
| **mean** | 5.843333 | 3.054000 | 3.758667 | 1.198667 |
| **std** | 0.828066 | 0.433594 | 1.764420 | 0.763161 |
| **min** | 4.300000 | 2.000000 | 1.000000 | 0.100000 |
| **25%** | 5.100000 | 2.800000 | 1.600000 | 0.300000 |
| **50%** | 5.800000 | 3.000000 | 4.350000 | 1.300000 |
| **75%** | 6.400000 | 3.300000 | 5.100000 | 1.800000 |
| **max** | 7.900000 | 4.400000 | 6.900000 | 2.500000 |

Looking at the above table, it is clear that all values have the same scale and ranges between 0 and 8 centimetres.
It means all data in data set do not require normalization to produce valuable results.

### Visualization of results

Having numeric variables in the data set allows creating easily multiple visual presentations of data.

The simple box and whisker plots of each variable present a clear idea of the distribution of the input attributes.

![Plot 1](Outputs/box_and_whisker_plot.png)

Using just one line of code ***dataset.hist()*** histogram of each input can be created.

![Histograms](Outputs/histogram.png)

The histogram demonstrates that two of the input variables have a [Gaussian distribution][2]. 

It is also extremely easy in Python (***scatter_matrix(dataset)***) to generate scatter matrix plot for each variable of iris data set.

![Scatter](Outputs/scatter.png)

Using Wikipedia [scatter][3] examples as references look like most of the scatter plots produced acceptable separations on the plots. The best separation of data that allows determining species is based on petal-width and petal-length and the worst is represented by sepal-length and sepal-width.

## Different analysis and approaches to the data set



## Going beyond the project and using more advanced Python tools


## Brief Python project program description

The Phyton program [segregation.py][1] was created to allow user basic interaction with the Iris data set. The program was updated a few times and evolved during this project creation. There are many approaches to load and read Iris data set in Python however in this basic program the solution that reflect final Project requirement was used. The Iris data set **iris.data** was downloaded from the UCI repository and it was not modified to a different format (csv and columns name) to show that Python can handle that kind of raw file. Mainly libraries like pandas and matplotlib were used to work on the data set.

To run this program the Python environment is required on the PC. Following steps help to setup software for the first run

* Install Python on your PC. You can use [Anaconda Distribution](https://www.anaconda.com/distribution/).  
* Use Command Prompt (you can use any console i.e. [Cmder](https://cmder.net/)) and navigate to the folder where you downloaded this repository programs.
* Type python "program name that you want to run" i.e. python segregation.py.

The program is loading data set in the background at the start from the folder Dataset and then welcome screen with "Menu" is displayed.

```python
Welcome to Programing and Scripting Project Program about the Iris Data Set.
This program contains the Iris data set which was automatically loaded into the program.
You can choose from the following menu option to display basic information and plot different graphs.

------------------------------ MENU ------------------------------
1. Display information about row and columns in data set
2. Display first 10 rows of segregated data
3. Display the statistical summary
4. Display box and whiskers plots
5. Display histogram of each input variable
6. Display scatter matrix plot
7. Exit
------------------------------------------------------------------
Enter your selection [1-7]:
```
In this section of code the ***def*** statement together with ***while*** loop and ***if*** condition was used to create **menu()** function. 

The first three menu options provide basic and statistical information about the data set and involve pandas libraries to carried out this task.

* ***print(dataset.shape)*** return dimensions and size of data frame. In this case number of rows and columns.
* ***print(dataset.head(10))*** display first ten rows of data set.
* ***print(dataset.describe())*** shows basic statistical details of data frame.

Next three positions of the menu (4-6) were clearly described in the [Visualization of results](#visualization-of-results) paragraph. 

The terminal window is going to be cleared after any selection from the menu regardless of the operating system. This involve **os** library.

```python
if os.name =="nt":
    cl = "cls"
else:
    cl = "clear"

os.system(cl)
```

Program is running continuously allows the user to make more choices from the menu until option seven is selected. This will terminate the program and display a goodbye message.

```python
Thank you for using this program :)
Goodbye!
```
 
## Conclution and summary



## References

1. [Wikipedia - Iris flower data set](https://en.wikipedia.org/wiki/Iris_flower_data_set)
1. [Iris Versicolor](https://www.lakeforest.edu/academics/programs/environmental/courses/es204/iris_versicolor.php)
1. [Iris Setosa](https://calphotos.berkeley.edu/cgi/img_query?enlarge=0000+0000+1202+1326)
1. [Iris Virginica](https://www.fs.fed.us/wildflowers/beauty/iris/Blue_Flag/images/iris_virginica_virginica_lg.jpg)
1. [Iris Data Set](http://mirlab.org/jang/books/dcpr/dataSetIris.asp?title=2-2%20Iris%20Dataset)
1. [UCI Machine Learning Repository - data set for this project](https://archive.ics.uci.edu/ml/datasets/iris)
1. [Wikipedia - Normal distribution](https://en.wikipedia.org/wiki/Normal_distribution)
1. [Watson Analytics Use Case: The Iris Data Set](https://www.ibm.com/communities/analytics/watson-analytics-blog/watson-analytics-use-case-the-iris-data-set/)
1. [Wikipedia - Scatter plot of Iris Data Set](https://en.wikipedia.org/wiki/Iris_flower_data_set#/media/File:Iris_dataset_scatterplot.svg)
1. [Pynative - Python function](https://pynative.com/python-check-user-input-is-number-or-string/)

[1]: segregation.py 
[2]: https://en.wikipedia.org/wiki/Normal_distribution
[3]: https://en.wikipedia.org/wiki/Iris_flower_data_set#/media/File:Iris_dataset_scatterplot.svg
