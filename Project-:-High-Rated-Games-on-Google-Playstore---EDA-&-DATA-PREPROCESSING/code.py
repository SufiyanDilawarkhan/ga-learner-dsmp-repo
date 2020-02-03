# --------------
#importing libraries
import pandas as pd
import numpy as numpy
import matplotlib.pyplot as plt
import seaborn as sns

#Loading the data
data = pd.read_csv(path)
data.head()

#Ploting histogram on 'Rating' column
plt.hist(data['Rating'].dropna())
plt.show

#Clean data by removing ratings greater than 5.
data = data[data['Rating'] <= 5]
data.head()


# --------------
# code starts here

total_null = data.isnull().sum()

percent_null = (total_null/data.isnull().count())

missing_data = pd.concat([total_null, percent_null], axis=1, keys=['Total','Percent'])

print (missing_data)

data = data.dropna()

total_null_1 = data.isnull().sum()

percent_null_1 = (total_null/data.isnull().count())

missing_data_1 = pd.concat([total_null_1, percent_null_1], axis=1, keys=['Total','Percent'])

print (missing_data_1)

# code ends here


# --------------
#Code starts here
chart = sns.catplot(x="Category",y="Rating",data=data, kind="box", height = 10)

chart.set_xticklabels(rotation=90)

chart.set_titles("Rating vs Category [BoxPlot]")

#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here
print (data['Installs'].value_counts())

data['Installs'] = data['Installs'].str.replace(",","")
data['Installs'] = data['Installs'].str.replace("+","")
data['Installs'] = data['Installs'].astype(int)

le = LabelEncoder()

data['Installs'] = le.fit_transform(data['Installs'])

regplot = sns.regplot(x="Installs", y="Rating", data=data)
regplot.set_title("Rating vs Installs [RegPlot]")

#Code ends here



# --------------
#Code starts here
print (data['Price'].value_counts())

data['Price'] = data['Price'].str.replace("$","")
data['Price'] = data['Price'].astype(float)

le = LabelEncoder()

data['Price'] = le.fit_transform(data['Price'])

regplot_price = sns.regplot(x="Price", y="Rating", data=data)
regplot_price.set_title("Rating vs Price [RegPlot]")
#Code ends here


# --------------
#Code starts here
data['Genres'].unique()

data['Genres'] = data['Genres'].str.split(';', n = 1, expand = True)[0]

gr_mean = data.groupby(["Genres"], as_index=False)["Rating", "Genres"].mean()

print (gr_mean.describe())

gr_mean = gr_mean.sort_values(by = "Rating")

print (gr_mean.iloc[0])
print (gr_mean.iloc[-1])

#Code ends here


# --------------
#Code starts here
print (data['Last Updated'].describe())

data['Last Updated'] = pd.to_datetime(data['Last Updated'])

max_date = max(data['Last Updated'])

data['Last Updated Days'] = (max_date - data['Last Updated']).dt.days

regplot_3 = sns.regplot('Last Updated Days','Rating',data=data)
regplot_3.set_title("Rating vs Last Updated [RegPlot]")

#Code ends here


