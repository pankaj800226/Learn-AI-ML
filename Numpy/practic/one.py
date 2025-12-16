print("--------------------------------------Hello Numpy----------------------------------------")

import numpy as np
# Student ID	Math	Science  	English

scores = np.array([
    [1, 88, 86, 53],
    [2, 92, 58, 80],
    [3, 80, 93, 83],
    [4, 83, 56, 100],
    [5, 59, 98, 91],
    [6, 69, 70, 59],
    [7, 97, 86, 98],
    [8, 92, 64, 84],
    [9, 76, 100, 93],
    [10,77, 64, 200],

])
print("Student Data\n",scores)

# 2 Show the shape of the scores array.
print(scores.shape)
print("Score",scores)

# 2 Get the Math score of student 5.
print(" Math score of student 5 : ",scores[4,1])

# 3 Calculate the average score for student 6.
average_score = np.mean(scores[5,1:])  # Student 6 is at index 5
print("average score for student 6: ",average_score)

# 4 Find the highest Science score.
highest_score = scores[:,2]
highest_score_and = np.max(highest_score)
print("highest Science score : ",highest_score_and)

# 5 Count how many students scored above 90 in English.
score_count = np.where(scores[:,3]>90)
print("Score count above 90 in english", score_count[0])

# 6. Find the student ID with the highest total score.
total_scores = np.sum(scores[:,1:], axis=1)  # Sum Math, Science, English for each student
highest_total_index = np.argmax(total_scores)
student_id_highest = scores[highest_total_index, 0]  # Get the student ID
print("Student with highest total score - ID:", student_id_highest, "Total:", total_scores[highest_total_index])

# 7. Calculate the mean score in each subject.

total_score1 = scores[:,1]
total_score2 = scores[:,2]
total_score3 = scores[:,3]

total_sum_student_score1 = np.sum(total_score1,axis=0)
total_sum_student_score2 = np.sum(total_score2)
total_sum_student_score3 = np.sum(total_score3)
# average score

total_sum_student_average = np.mean(total_score1)

print("total sum column 1 ", total_sum_student_score1)
print("total sum column 2  ", total_sum_student_score2)
print("total sum column 3 ", total_sum_student_score3)
print("total average ", total_sum_student_average)

# 8. Sort students by Math score (descending).
sort_math_score = scores[:,1]
sort_math_score_ans = np.sort(sort_math_score)[::-1]  # Reverse for descending ord
print("sort_math_score_ans ",sort_math_score_ans)

# 9. Get the top 3 Science scores and their student IDs.
science_score = scores[:,2]
top3_science = np.argsort(science_score)[-3:]
print("top3_science : ", top3_science)













