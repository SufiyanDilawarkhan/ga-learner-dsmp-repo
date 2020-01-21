# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Loading the dataframe using pd.read_csv() and storing the dataframe in a variable called data.
data = pd.read_csv(path)

#Saving the value counts of Loan_Status in a variable called loan_status using value_counts().
loan_status = data['Loan_Status'].value_counts()

#Plotting a bar graph of loan_status.
loan_status.plot(kind = 'bar')

#Display chart.
plt.show()

#Code starts here


# --------------
#Code starts here

#Grouping the 'data' dataframe by Property_Area and Loan_Status and storing it in a variable called 'property_and_loan'
#Using the .size() method on 'property_and_loan' and then using .unstack()
property_and_loan = data.groupby(['Property_Area', 'Loan_Status']).size().unstack()

#Plotting an unstacked bar plot of property_and_loan
property_and_loan.plot(kind = 'bar', stacked = False)

#Naming the x-axis as Property Area
plt.xlabel('Property Area')

#Naming the y-axis as Loan Status
plt.ylabel('Loan Status')

#Rotating the labels of x-axis by 45°
plt.xticks(rotation = 45)


# --------------
#Code starts here

#Grouping the 'data' dataframe by Education and Loan_Status and storing it in a variable called 'education_and_loan'.
#Using the .size() method on 'education_and_loan' and then using .unstack()
education_and_loan = data.groupby(['Education', 'Loan_Status']).size().unstack()

#Plotting a stacked bar plot of education_and_loan.
education_and_loan.plot(kind = 'bar', stacked = True)

#Naming the x-axis as Education Status.
plt.xlabel('Education Status')

#Naming the y-axis as Loan Status.
plt.ylabel('Loan Status')

#Rotating the labels of x-axis by 45°.
plt.xticks(rotation = 45)


# --------------
#Code starts here

#Creating a dataframe called 'graduate' which is a subset of 'data' dataframe with the condition "data['Education'] == 'Graduate'"
graduate = data[data['Education'] == 'Graduate']

#Creating a dataframe called 'not_graduate' which is a subset of 'data' dataframe with the condition "data['Education'] == 'Not Graduate'"
not_graduate = data[data['Education'] == 'Not Graduate']

#Plotting a density plot LoanAmount of 'graduate' dataframe using "Series.plot()" and passing the parameter kind='density' and label='Graduate'
graduate.LoanAmount.plot(kind = 'density', label = 'Graduate')

#Plotting a density plot LoanAmount of 'not_graduate' dataframe using "Series.plot()" and passing the parameter kind='density' and label='Not Graduate'
not_graduate.LoanAmount.plot(kind = 'density', label = 'Not Graduate')


#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here

#Creating three subplots with (nrows = 3 , ncols = 1) and storing it in variable's fig ,(ax_1,ax_2,ax_3)
fig, (ax_1, ax_2, ax_3) = plt.subplots(nrows = 3, ncols = 1)

#Plotting scatter plot between 'ApplicantIncome' and LoanAmount using ax_1.set axis title as Applicant Income.
data.plot.scatter(x = 'ApplicantIncome', y = 'LoanAmount')
ax_1.set_title('Applicant Income')

#Plotting scatter plot between 'CoapplicantIncome' and LoanAmount using ax_2.set axis title as Coapplicant Income
data.plot.scatter(x = 'CoapplicantIncome', y = 'LoanAmount')
ax_2.set_title('Coapplicant Income')

#Creating a new column in the dataframe called 'TotalIncome' which is a sum of the values of columns ApplicantIncome and CoapplicantIncome
data['TotalIncome'] = data['ApplicantIncome'] + data['CoapplicantIncome']

#Plotting scatter plot between 'TotalIncome' and LoanAmount using ax_3.set axis title as Total Income
data.plot.scatter(x = 'TotalIncome', y = 'LoanAmount')
ax_3.set_title('Total Income')


