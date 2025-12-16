import numpy as np

# Columns: [ID, Year, Rating, Duration(min), Votes(in thousands)]
movies = np.array([
    [1, 1994, 9.3, 142, 2300],
    [2, 1972, 9.2, 175, 1600],
    [3, 2008, 9.0, 152, 2500],
    [4, 1999, 8.8, 136, 1700],
    [5, 2010, 8.7, 148, 2100],
    [6, 1994, 8.9, 154, 1800],
])


#1. Normalize the Votes column using max normalization
votes = movies[:,4]
min_val = np.min(votes)
max_val = np.max(votes)
normalized_votes  = (votes - min_val) / (max_val - min_val)
print("Normalized Votes (Min-Max):", normalized_votes)


# Find the movie with the highest rating
hei_rating = np.argmax(movies[:,3])
print("Height movies rating : ",hei_rating)

# Find movies released after 2000
released_data = np.where(movies[:,1]>2000)
print("movies released after 2000 :",released_data[0])

# Calculate average movie duration
average_movies = np.mean(movies[:,3],axis=0)
print("Calculate average movie duration :",average_movies)

# 6. Sort movies by votes (descending)
movies_sort_vote = np.sort(movies[:,4])
print("Sort movies by votes (descending) :",movies_sort_vote)