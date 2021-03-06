# -*- coding: utf-8 -*-
"""CS210 Template.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/194FWvzbaRxlW0l6LIJgYZbD7zW3DB9vO

<font color="red">IMPORTANT</font>

<font color="red">This is just a template for your project reports. You do not have to use the exact structure here. You may add your own sections/subsections. However, you are required to preserve the same report flow.</font>

# SALARY ESTIMATOR FOR MBA GRADUATES  - Group 36

Group Members:

Ural Sarp Sipahi

Bartu Doğan

Muammer Tunahan Yıldız

Egemen Aydın

Rıza Lider Büyükçanak
"""

# Egemen:  Üstünkörü, proposaldakiyle aynı olmasın diye yazdım. dursun diye öyle.

"""(1) a high-quality introduction on what you are doing, why you are doing it

-	We are developing a machine Learning program that takes parameters(features) from the user as input and
	give an estimate salary expectation for given feature values. The reason we are doing this program is
	being able to have an opinion and understanding on the criterias that affect MBA graduates salaries.
	Also determining the criterias that affect the final salary most and the least.

(2) a clear description of the datasets you have used

-	We used the Campus Recruitment dataset. The dataset includes the percentages of each individual students at 
	10th and 12th grade (high-school) with their specilizations. Moreover, dataset provides us students Undergraduate
	degree specilziation and its percentage (GPA) too. MBA specilization and GPA is included in the dataset either.
	In the dataset despite students academic features, genders and wether they have work experience or not
	are specified too. Lastly, Employibility test scores which are conducted by colleges, and information of 
	whether the person is placed into a job or not, and if they are placed, their salaries."""

"""## Introduction

<font color="blue">
Main goal of this project is to create a Machine Learning program that is trained
with various data collected from the campus recruitment dataset in order to
estimate the salaries of Master of Business Administration graduates as
accurately as possible.
</font>

### Problem Definition

<font color="blue">
State your problem in technical terms. What is your end goal? How are you going to solve it?


</font>

### Utilized Datasets

<font color="blue">
Describe the utilized datasets in detail. Provide the data source (links if possible), number of obervations, data types, display the distributions of various variables and plot figures that helps reader understand what you are dealing with.
</font>


https://www.kaggle.com/benroshan/factors-affecting-campus-placement
"""

from google.colab import drive
drive.mount('./drive', force_remount=True)

path_prefix = './drive/My Drive'

# Commented out IPython magic to ensure Python compatibility.
# Libraries that we may use in the future: 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from os.path import join
import json
import seaborn as sns
import sys
import warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")
# %matplotlib inline

"""Campus Recruitment Dataset"""

fname = 'Placement_Data_Full_Class.csv'
df = pd.read_csv(join(path_prefix, fname))
df.head(3)

"""Data cleaning by dropping the rows with null values"""

df2=df[df['salary'].isnull()]
df = df.dropna() #df doesnt contain missing values.
#df2.head(3)      df2 only contains rows that have salary NaN.

df.head(3)

df3 = df.copy() # egemen: df with students without salaries.

df3 = df3.dropna(axis="index", how="any")

df3.describe()

"""Feature generation by """

df3 = df3[['gender', 'ssc_p',  'hsc_p' ,  'degree_p','degree_t','workex','etest_p','specialisation','mba_p','salary']]

df3 = df3.reset_index()
df3 =  df3.drop(columns=['index'])

df3.head()

df3['highs_p'] = (df3['ssc_p'] + df3['hsc_p']) / 2

df3.head()

df3 = df3.drop(columns=['ssc_p','hsc_p'])

df3.head()

df3.info()

#salary distrubution:
ax = sns.distplot(df3["salary"])
ax.set_title("Salary Distribution")
ax.grid()
plt.show()

"""## Data Exploration

<font color="blue">
Explore the relationship between different variables across datasets. Perform hypothesis tests if necessary. Comment on your resulting figures and findings.

This section corresponds to the work you have done in the progress report.
</font>
"""

ax = sns.boxplot(x="specialisation", y="salary", data=df3[["specialisation","salary"]], palette='Set1',showfliers = False)
ax.set_title('Salary Distribution with Specialisation Type')
plt.show()

# extreme values are not shown in the figure

"""It can be seen from the graph that people who have specialized on marketing & finance get slightly better salaries overall compared to the people who have specialized in marketing & HR"""

ax = sns.violinplot(x="degree_t", y="salary", data=df3[["degree_t","salary"]], palette='Set1')
ax.set_title('Salary Distribution with Degree Type')
plt.show()

"""It can be seen from the graph that people who have graduated in the area of science and technology get more salary in average than people who graduated from management or other areas. However it can also be seen from the graph that there are management graduates who get more salary than science and technology graduates."""

ax = sns.boxplot(x="gender", y="salary", data=df3[["gender","salary"]], palette='Set1',showfliers = False)
ax.set_title('Salary Distribution with Gender Type')
plt.show()

"""It can be seen from the graph that females have wider distribution in their salaries compared to males. One can also conclude from the graph that males generally get more salary than females."""

ax0 = sns.violinplot(x="gender", y="salary", data=df3[["gender","salary"]], palette='Set1')
ax0.set_title('Salary Distribution with gender')
plt.show()

ax2 = sns.scatterplot(x="highs_p", y="salary", data=df3[["highs_p","salary"]], palette='Set1')
ax2.set_title('Salary Distribution with highs_p')
plt.show()

"""The scatterplot above does not show a clear correlation between salary and high-school grades. The average salary is distributed relatively even amongst people who got grades from 55 to 80. The graph also shows that the person who got the highest grade does not get the highest salary therefore we cannot make any assumptions such as the person who got the lowest grade in high-school will get the lowest salary or vice versa."""

ax7 = sns.scatterplot(x="degree_p", y="salary", data=df3[["degree_p","salary"]], palette='Set1')
ax7.set_title('Salary Distribution with Under Graduate Degree Percentages')
#ax7.set(xlim=(45, 100))
plt.show()

ax8 = sns.violinplot(x="degree_t", y="salary", data=df3[["degree_t","salary"]], palette='Set1')
ax8.set_title('Salary Distribution with Under Graduation Degree Types')
plt.show()

ax9 = sns.violinplot(x="workex", y="salary", data=df3[["workex","salary"]], palette='Set1')
ax9.set_title('Salary Distribution with Work Experience')
plt.show()

"""It can be seen that people who have work experience are able to gain higher salaries that their counterparts who have no work experience. """

ax10 = sns.scatterplot(x="etest_p", y="salary", data=df3[["etest_p","salary"]], palette='Set1')
ax10.set_title('Salary Distribution with Employability test percentage')
ax10.set(xlim=(45, 100))
plt.show()

"""Here we can see that the correlation between Employability test results and each individual's current salary. There is a positive correlation between these two parametres, which can be understood that employability tests give clues of an employee's expected salary."""

ax11 = sns.violinplot(x="specialisation", y="salary", data=df3[["specialisation","salary"]], palette='Set1')
ax11.set_title('Salary Distribution with Specialisation')
plt.show()

"""The two violin plots show students' specialisation areas after graduating from MBA. Including the extreme values, it is clear that students' who specialised in Finance area are expected to have higher salaries against students who specialized in Human Resources. It is easier to estimate the salary of students who specialized in HR area due to the fact that left plot's daha yayvan olmak(?) of the highest probability parts of the plot and there are less extreme values.

## Machine Learning Models

<font color="blue">
This is the section that you primarily need work on for the final report. Implement at least two machine learning models so that you can compare them.
</font>
"""

# bartu
length = 148
from sklearn import datasets, linear_model
x = df.etest_p.values
y = df.salary.values
x = x.reshape(length, 1)
y = y.reshape(length, 1)

regr = linear_model.LinearRegression()
regr.fit(x, y)

plt.scatter(x, y)
plt.plot(x, regr.predict(x))
plt.xticks(())
plt.yticks(())
plt.show()

#sarp  bir şeyler denedim de olmadı
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder


encoder=LabelEncoder()

for col in df.columns:
   if df[col].dtype == 'object':
     encoder.fit(df[col])
     df[col] = encoder.transform(df[col])

Y=df['salary']

X=df.drop(['salary','status','sl_no'],axis=1)
X=pd.get_dummies(X)


# 80% for training and 20% for testing-validation
X_train, X_remaining, y_train, y_remaining = train_test_split(X, Y, test_size=0.20, random_state=42)
# 10% validation, 10% test
X_test, X_val, y_test, y_val = train_test_split(X_remaining, y_remaining, test_size=0.50, random_state=42)



lr=LinearRegression()
lr.fit(X_train,y_train)

print('Linear Regression score is:' + str(lr.score(X_test, y_test)))

"""### Implementation

<font color="blue">
Implement and evaluate your models. Perform hyperparameter tunning if necessary. Choose the correct evaluation metrics.
</font>

### Results & Discussion

<font color="blue">
Display and discuss the results of your models. Deploy tables, figures etc. to present your results. Discuss the advantages/disadvantages of models compared to each other.
</font>

## Conclusion

<font color="blue">
Briefly evaluate your project. Is your solution applicable? What are the advantages/disadvantages of your solution?
</font>

## Future Work

<font color="blue">
In the progress report, clearly state your goals for the final report.<br>
In the final report, articulate on the future directions, scenarios.
</font>

## Work Division



<font color="blue">
A clear description of the division of work among teammates.
</font>
"""