# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode

# code starts here

#Reading the file and creating a dataframe bank by passing the path of the file
bank = pd.DataFrame(pd.read_csv(path))

#Create the variable 'categorical_var' and using 'df.select_dtypes(include = 'object')' check all categorical values.
categorical_var = bank.select_dtypes(include = 'object')

#Print 'categorical_var'
print (categorical_var)

#Create the variable 'numerical_var' and using 'df.select_dtypes(include = 'number')' check all categorical values.
numerical_var = bank.select_dtypes(include = 'number')

#Print 'numerical_var'
print (numerical_var)

# code ends here


# --------------
# code starts here

#From the dataframe 'bank', drop the column 'Loan_ID' to creating a new dataframe 'banks'
banks = bank.drop(columns = 'Loan_ID')

#Using "isnull().sum()" function to find null values and printing it.
print (banks.isnull().sum())

#Calculating mode for the dataframe 'banks' and storing in 'bank_mode'
bank_mode = banks.mode().iloc[0]

#Filling missing(NaN) values of 'banks' with 'bank_mode' and storing the cleaned dataframe back in 'banks'.
banks.fillna(bank_mode, inplace = True)

#Checking if all the missing values (NaN) are filled.
print (banks.isnull().sum())

#code ends here


# --------------
# Code starts here

avg_loan_amount = banks.pivot_table(values = ['LoanAmount'], index = ['Gender', 'Married', 'Self_Employed'], aggfunc = np.mean)
avg_loan_amount

# code ends here



# --------------
# code starts here

#Creating variable 'loan_approved_se' and storing the count of results where Self_Employed == Yes and Loan_Status == Y.
loan_approved_se = banks.loc[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y'), ['Loan_Status']].count()
print (loan_approved_se)

#Creating variable 'loan_approved_nse' and storing the count of results where Self_Employed == No and Loan_Status == Y.
loan_approved_nse = banks.loc[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y'), ['Loan_Status']].count()
print (loan_approved_nse)

#Calculating percentage of loan approval for self employed people and storing result in variable 'percentage_se'. Loan_Status count is given as 614.
percentage_se = loan_approved_se * 100 / 614
percentage_se = percentage_se[0] 
print (percentage_se)   

#Calculating percentage of loan approval for people who are not self-employed and storing the result in variable 'percentage_nse'. Loan_Status count is given as 614.
percentage_nse = loan_approved_nse * 100 / 614
percentage_nse = percentage_nse[0]
print (percentage_nse)

# code ends here


# --------------
# code starts here

#Using "apply()"function to convert Loan_Amount_Term which is in months to year and storing the result in a variable 'loan_term'.
loan_term = banks['Loan_Amount_Term'].apply(lambda x : int(x) / 12)
print (loan_term)

#Finding the number of applicants having loan amount term greater than or equal to 25 years and storing them in a variable called 'big_loan_term'.
big_loan_term = len(loan_term[loan_term >= 25] == True)
print (big_loan_term)

# code ends here


# --------------
# code starts here

#Groupingby the 'banks' dataframe by Loan_Status and storing the result in a variable called 'loan_groupby'
loan_groupby = banks.groupby(['Loan_Status'])

#Subsetting 'loan_groupby' to include only ['ApplicantIncome', 'Credit_History'] and storing the subsetted dataframe back in 'loan_groupby'
loan_groupby = loan_groupby[['ApplicantIncome', 'Credit_History']]

#finding the mean of 'loan_groupby'and storing the result in a new variable 'mean_values'
mean_values = loan_groupby.mean()
print (mean_values)

# code ends here


