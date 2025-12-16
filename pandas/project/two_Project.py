import pandas as pd 

df = pd.read_csv('Books_cleaning_data_done.csv')
print(df)
print(df.head(5))
print(df.tail(5))
print(df.shape)
print(df.info)
print(df.isna().sum())
print(df.dtypes)
print(df.columns)
print(df)

print("duplicare")
print(df.duplicated().sum())
