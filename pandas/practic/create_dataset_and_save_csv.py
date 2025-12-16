
import pandas as pd
import numpy as np
data={
    "Name":["Ram","Gita","Sita"],
    "Age":[23,23 ,40],
    "City":["Delhi","Mumbai","Kolkata"]
}

df = pd.DataFrame(data)

print(df)

df.to_csv("csv_data.csv",index=False)
print(df.info())
print("duplicated")
df[df.duplicated()]
print(df)