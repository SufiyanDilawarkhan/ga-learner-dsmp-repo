# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
#data = np.genfromtxt('path', delimiter=',', skip_header=1)
#print (data)

#data_file='file.csv' # path for the file
data=np.genfromtxt(path, delimiter=",", skip_header=1)

print("\nData: \n\n", data)

print("\nType of data: \n\n", type(data))

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here

census = np.concatenate([data, new_record])
print (census)


# --------------
#Code starts here

age = np.array(census[:,0])
print (age)

max_age = np.max(age)
print(max_age)

min_age = np.min(age)
print(min_age)

age_mean = np.mean(age)
print (age_mean)

age_std = np.std(age)
print (age_std)


# --------------
#Code starts here

#Find lengths on each races

race_0 = census[census[:,2] == 0]
print (race_0)
len_0 = len(race_0)
print (len_0)

race_1 = census[census[:,2] == 1]
print (race_1)
len_1 = len(race_1)
print (len_1)

race_2 = census[census[:,2] == 2]
print (race_2)
len_2 = len(race_2)
print (len_2)

race_3 = census[census[:,2] == 3]
print (race_3)
len_3 = len(race_3)
print (len_3)

race_4 = census[census[:,2] == 4]
print (race_4)
len_4 = len(race_4)
print (len_4 )

#Collating all races in one variable 
races = [len_0, len_1, len_2, len_3, len_4]

#Finding the minority race having minimum length
minority_race = races.index(min(races))

print (minority_race)



# --------------
#Code starts here

#Subsetting array census based on age above 60
senior_citizens = census[census[:,0]>60]

#Calculating the sum of hours worked (Sum of all values of the array)
working_hours_sum = senior_citizens.sum(axis=0)[6]

#Calculating the lenth of the array of senior citizens (Finding the number of senior citizens)
senior_citizens_len = len(senior_citizens)

#Finding the average working hours of the senior citizens
avg_working_hours = working_hours_sum / senior_citizens_len
print (avg_working_hours)


# --------------
#Code starts here

#Finding education higher than 10 by subsetting census array
high = census[census[:,1] > 10]

#Finding education lower than or equal to 10 by subsetting census array
low = census[census[:,1] <= 10]

#Calculating average high pay using mean function
avg_pay_high = high[:,7].mean()
print (avg_pay_high)

#Calculating average low pay using mean function
avg_pay_low = low[:,7].mean()
print (avg_pay_low)


