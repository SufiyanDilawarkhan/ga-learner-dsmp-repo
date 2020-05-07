### Project Overview

 **Problem Statement**

For this project I have explored the publicly available data from LendingClub.com. Lending Club connects people who need money (borrowers) with people who have money (investors). As an investor one would want to invest in people who showed a profile of having a high probability of paying the amount back.

The data that we have is from 2007-2010.

Using Decision Tree model, I classified whether or not the borrower paid back their loan in full.


The dataset has details of 9578 customers with the following features:

- Feature	- Description
- customer.id	- ID of the customer
- credit.policy	- If the customer meets the credit underwriting criteria of LendingClub.com or not
- purpose	- The purpose of the loan(takes values :"creditcard", "debtconsolidation", "educational", "majorpurchase", "smallbusiness", and "all_other").
- int.rate	- The interest rate of the loan
- installment	- The monthly installments owed by the borrower if the loan is funded
- log.annual.inc	- The natural log of the self-reported annual income of the borrower
- dti	- The debt-to-income ratio of the borrower (amount of debt divided by annual income)
- fico	- The FICO credit score of the borrower
- days.with.cr.line	- The number of days the borrower has had a credit line.
- revol.bal	- The borrower's revolving balance (amount unpaid at the end of the credit card billing cycle)
- revol.util	- The borrower's revolving line utilization rate (the amount of the credit line used relative to total credit available)
- pub.rec	- The borrower's number of derogatory public records (bankruptcy filings, tax liens, or judgments)
- inq.last.6mths	- The borrower's number of inquiries by creditors in the last 6 months
- delinq.2yrs	- The number of times the borrower had been 30+ days past due on a payment in the past 2 years
- paid.back.loan	- Whether the user has paid back loan


### Learnings from the project

 After completing this project, I have a better understanding of how to build a decision tree model. In this project, I have applied the following concepts.

- Train-Test Split
- Correlation between the Features
- Decision Tree Modeling
- Evaluation Metrics
- Graphviz Plotting


### Approach taken to solve the problem

 My approach was:

- Data Loading - Loaded the data and also droped certain columns and split the data for further tasks.
- Target Variable Distribution - Took a look at the distribution of target variable 'paid.back.loan'.
- Feature Spliting - Feature engineering by splitting the features based on the data type for visualization purposes.
- Numerical Features Visualisation - Plotted and saw the relation of numerical features with the target variable.
- Categorical Features Visualisation - Plotted and saw the relation of categorical features with the target variable.
- Model Building - Modelled Decision Tree.
- Decision Tree Pruning - Checked if pruning of decision tree improves its accuracy. Used grid search to do the optimum pruning.
- Tree visualising - Saw how the pruned decision tree looked like using graphviz.


