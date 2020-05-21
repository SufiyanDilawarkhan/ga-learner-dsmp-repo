# --------------
import pandas as pd
from sklearn.model_selection import train_test_split
#path - Path of file 

# Code starts here

df = pd.read_csv(path)

X = df.iloc[:, 1:-1]
y = df.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)


# --------------
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Code starts here

X_train['TotalCharges'] = X_train['TotalCharges'].replace(" ", np.NaN)
X_test['TotalCharges'] = X_test['TotalCharges'].replace(" ", np.NaN)

X_train['TotalCharges'] = X_train['TotalCharges'].astype(float)
X_test['TotalCharges'] = X_test['TotalCharges'].astype(float)

X_train['TotalCharges'] = X_train['TotalCharges'].fillna(X_train['TotalCharges'].mean())
X_test['TotalCharges'] = X_test['TotalCharges'].fillna(X_test['TotalCharges'].mean())

X_train.isnull().sum()
y_train.isnull().sum()

categorial_features = X_test.select_dtypes(include=['object']).columns.values.tolist()
le = LabelEncoder()
for i in range(0, len(categorial_features)):
    le.fit(X_train[categorial_features[i]])
    X_train[categorial_features[i]]=le.transform(X_train[categorial_features[i]])
    X_test[categorial_features[i]]=le.transform(X_test[categorial_features[i]])

y_train = y_train.replace({'No':0,'Yes':1})
y_test = y_test.replace({'No':0,'Yes':1})


# --------------
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

# Code starts here
#print (X_train, X_test, y_train, y_test)

ada_model = AdaBoostClassifier(random_state = 0)

ada_model.fit(X_train, y_train)

y_pred = ada_model.predict(X_test)

ada_score = accuracy_score(y_test, y_pred)

print ("Ada Score = ",ada_score)

ada_cm = confusion_matrix(y_test, y_pred)

print ("\nConfusion Matrix", ada_cm)

ada_cr = classification_report(y_test, y_pred)

print ("\nClassification Report",ada_cr)


# --------------
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV

#Parameter list
parameters={'learning_rate':[0.1,0.15,0.2,0.25,0.3],
            'max_depth':range(1,3)}

# Code starts here
xgb_model = XGBClassifier(random_state = 0)

xgb_model.fit(X_train, y_train)

y_pred = xgb_model.predict(X_test)

xgb_score = accuracy_score(y_test, y_pred)

print ("XGBoost Score = ",xgb_score)

xgb_cm = confusion_matrix(y_test, y_pred)

print ("\nXGBoost Confusion Matrix = ",xgb_cm)

xgb_cr = classification_report(y_test, y_pred)

print ("\nXGBoost Classification Report = ",xgb_cr)

xgb_clf = XGBClassifier(random_state=0)
clf_model = GridSearchCV(estimator = xgb_clf, param_grid = parameters)

clf_model.fit(X_train, y_train)

y_pred = clf_model.predict(X_test)

clf_score = accuracy_score(y_test, y_pred)

print (clf_score)

clf_cm = confusion_matrix(y_test, y_pred)

print (clf_cm)

clf_cr = classification_report(y_test, y_pred)

print (clf_cr)




