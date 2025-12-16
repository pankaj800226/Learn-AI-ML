import pandas as pd
# import numpy as np
df = pd.read_csv('employee_dirty_dataset.csv')
print(df)
print(df.shape)

insert_bonus = df.insert(5,"Bonus",[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000,12000])
print("Add a Bonus point ")
print(insert_bonus)
print(df.shape)

c = df[df["Salary"]> 50000]
print("above 50000")
print(c)

d = df[["Name","Salary",'Bonus']]
print("Name print")
print(d)

n = df[(df["Salary"]>50000) & (df["Bonus"]>3000)]
print("select salary and bonus")
print(n)

# remove duplicate name 
df = df.drop_duplicates(subset="Name")


# replace NaN value
df['Age'] = df["Age"].replace('Thirty', 30)
df = df.dropna(subset='Age')


# cleane numeric data value
# df['Age'] = df['Age'] = pd.to_numeric(df['Age'],errors='coerce')
df['Age'] = pd.to_numeric(df['Age'],errors='coerce')

df = df.dropna(subset='Department')

# salary cleane
# df = df.dropna(subset=['Salary'])
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())


# cleane JoiningDate
df["JoiningDate"] = pd.to_datetime(df['JoiningDate'],errors='coerce')
df = df.dropna(subset=['JoiningDate'])

# city nan 

df = df.dropna(subset=['City'])

df = df[(df["Salary"]>10000)& (df["Salary"]<1000000)]

df.to_csv('cleaned_employee_dataset.csv',index=False)
print("Cleaning the data save in dataset 'cleaned_employee_dataset.csv'")

print("\n final cleaning done")
print(df)



