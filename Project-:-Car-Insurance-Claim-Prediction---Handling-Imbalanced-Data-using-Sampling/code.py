# --------------
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Code starts here
df = pd.read_csv(path)

print (df.iloc[:, :5].head())

print (df.info())

cols = ['INCOME','HOME_VAL','BLUEBOOK','OLDCLAIM','CLM_AMT']

for c in cols:
    df[c] = df[c].str.replace("$", "")
    df[c] = df[c].str.replace(",", "")

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

print (y.value_counts())

X_train,X_test,y_train,y_test = train_test_split(X, y, test_size = 0.3, random_state = 6)

# Code ends here


# --------------
# Code starts here

cols1 = ['INCOME','HOME_VAL','BLUEBOOK','OLDCLAIM','CLM_AMT']

for c1 in cols1:
    X_train[c1] = X_train[c1].astype(float)
    X_test[c1] = X_test[c1].astype(float)

print (X_train.isnull().sum())
print (X_test.isnull().sum())

# Code ends here


# --------------
# Code starts here
X_train.dropna(subset = ['YOJ','OCCUPATION'], inplace = True)
X_test.dropna(subset = ['YOJ','OCCUPATION'], inplace = True)

y_train = y_train[X_train.index]
y_test = y_test[X_test.index]

cols2 = ['AGE','CAR_AGE','INCOME', 'HOME_VAL']
for c2 in cols2:
    X_train[c2] = X_train[c2].fillna(X_train[c2].mean())
    X_test[c2] = X_test[c2].fillna(X_test[c2].mean())

# Code ends here


# --------------
from sklearn.preprocessing import LabelEncoder
columns = ["PARENT1","MSTATUS","GENDER","EDUCATION","OCCUPATION","CAR_USE","CAR_TYPE","RED_CAR","REVOKED"]
le = LabelEncoder()

# Code starts here
for c in columns:
    X_train[c] = le.fit_transform(X_train[c])
    X_test[c] = le.fit_transform(X_test[c])

print (X_train.head())
print (X_test.head())

# Code ends here



# --------------
from sklearn.metrics import precision_score 
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

# code starts here 
model = LogisticRegression(random_state = 6)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

score = accuracy_score(y_test, y_pred)

print ("Accuracy Score =",score)

# Code ends here


# --------------
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

# code starts here
smote = SMOTE(random_state = 9)

X_train, y_train = smote.fit_sample(X_train, y_train)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Code ends here


# --------------
# Code Starts here
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

score = accuracy_score(y_test, y_pred)
print ("Accuracy Score with SMOTE = ",score)

# Code ends here


