# Data structure [resturent _id,2021,2022,2023,2024]
import numpy as np
import matplotlib.pyplot as plt


sales_data = np.array([
 [1,150000,180000,220000,100000], # Bririyani
 [2,120000,140000,160000,200000], # bejijing bites
 [3,200000,230000,260000,300000], # bejijing bites
 [4,180000,210000,170000,210000], # Pizza
 [5,110000,280000,190000,280000], # cholla
])

print("=== Zomato Data ===")
print(sales_data.shape)
print("simple data 1st 3 resturent : ", sales_data[0:3])

arange_data = np.sort(sales_data)
print("arangeing sales data : ",arange_data)

#find out min price in data
min_price_sale = np.min(sales_data[:,1:],axis=1)
print("min sale : ", min_price_sale)

# find out max price in data
max_price_sale = np.max(sales_data[:,1:],axis=1)
print("max sale : ", max_price_sale)

# check all array in largest amount
print(np.max(sales_data[:]))

