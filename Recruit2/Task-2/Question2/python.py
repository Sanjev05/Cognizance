import pandas as pd
df = pd.read_csv("/Users/sanjevr/Documents/GitHub/Cognizance/Recruit2/Task-2/Question2/Dataset.csv")
#print(df.head())
print(df.isnull().sum())
print(" To print the columns which contains NaN values...")
for i in df.columns:
    if df[i].isnull().sum() != 0:
        print(i)
# dropping NaN values => df.dropna()
# Filling NaN values with any value => df.fillna("value")
df1 = df.copy()
#we have made a copy of the data set so that the original data set remains unchanged!!!
# Dropping NaN values...
df1 = df1.dropna()
print("After removing all the Nan value the sum of all the Nan values is zero")
print(df1.isnull().sum().sum())
# Filling NaN values...
#Here we have made another copy of the data set but we have replaced the Nan values with Zero
df2 = df.copy()
df2.fillna(0, inplace=True)
print("After replacing all the Nan values with zero the sum of all the Nan value becomes Zero!!")
print(df2.isnull().sum().sum())