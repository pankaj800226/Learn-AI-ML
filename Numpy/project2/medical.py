import numpy as np

# Patient ID	Age	Blood Pressure (mmHg)	Heart Rate (bpm)	Glucose Level (mg/dL)
data = np.array([
    [1, 25, 120, 80, 90],
    [2, 60, 140, 70, 160],
    [3, 45, 130, 75, 120],
    [4, 35, 110, 85, 95],
    [5, 50, 150, 72, 180],
    [6, 40, 135, 76, 110],
    [7, 30, 125, 82, 100],
    [8, 55, 145, 68, 170],
    [9, 28, 118, 88, 92],
    [10, 65, 160, 65, 200]
])


# Find the average age of all patients.
average_age = np.mean(data[:,1],axis=0)
print(average_age)

# Select patients whose blood pressure is greater than 140.
heigh_blood = np.where(data[:,2]>140)
print("heigh blood pressure patient id : ",data[heigh_blood,0])

# Find the IDs of patients with glucose level above 150.
level = np.where(data[:,4]>150)
print("glucose level above 150 : ",data[level,0])

# Normalize the glucose column using min normalization.
min_glucose = np.min(data[:,4],axis=0)
print("min value glucose column ",min_glucose)

# Normalize the glucose column using max normalization.
max_glucose = np.max(data[:,4],axis=0)
print("max value glucose column ",max_glucose)

# Sort the patients in increasing order of heart rate.
sorting_data = np.sort(data[:,1:])
print("Data sorting ",sorting_data)





