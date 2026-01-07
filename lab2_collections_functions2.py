# Lab 2: Python Basics – Working with Collections & Functions
# Unique names + clear comments explaining every step
# -------------------------

# -------------------------
# Part 1: Tuples
# -------------------------

# 1. Create and Access
# Define a tuple with 5 numerical values
speed_factors = (11, 22, 33, 44, 55)

# Access the third item (index 2)
print("Third speed factor:", speed_factors[2])

# 2. Tuple Modification (Workaround)
# Convert tuple to list to remove an item, then convert back to tuple
speed_list = list(speed_factors)  # Convert tuple to list
speed_list.remove(33)             # Remove the value 33 from list
adjusted_speeds = tuple(speed_list)  # Convert back to tuple
print("Adjusted speeds after removal:", adjusted_speeds)

# 3. Tuple Unpacking
# Assign each element of the tuple to individual variables
planet_masses = (101, 202, 303, 404, 505)
mercury, venus, earth, mars, jupiter = planet_masses
print("Unpacked planet masses:", mercury, venus, earth, mars, jupiter)

# 4. Tuple to String
# Convert a tuple of characters into a single string
greeting_chars = ('H', 'e', 'l', 'l', 'o')
greeting_word = ''.join(greeting_chars)
print("Greeting word:", greeting_word)

# 5. Find Duplicates
# Identify duplicates in a tuple
lucky_numbers = (7, 14, 7, 21, 28, 14, 35)
# Use list comprehension and set to find repeated values
repeats_found = set([n for n in lucky_numbers if lucky_numbers.count(n) > 1])
print("Repeated numbers in lucky_numbers:", repeats_found)

# 6. Reverse Tuple
# Print tuple in reverse order using slicing
print("Reversed speed factors:", speed_factors[::-1])

# -------------------------
# Part 2: Lists
# -------------------------

# 7. Sum of List
# Sum all items in a list of numbers
daily_steps = [5000, 7500, 8000, 6200, 7000]
total_steps = sum(daily_steps)
print("Total steps this week:", total_steps)

# 8. Remove Duplicates (Maintain Order)
# Create a new list without duplicates
visited_countries = ['Nigeria', 'Ghana', 'Nigeria', 'Kenya', 'Ghana']
unique_countries = []
for country in visited_countries:
    if country not in unique_countries:
        unique_countries.append(country)
print("Unique countries visited:", unique_countries)

# 9. Clone a List
# Show three different ways to copy a list
favorite_colors = ['red', 'green', 'blue']
copy1 = favorite_colors.copy()  # Using list copy method
copy2 = list(favorite_colors)   # Using list constructor
copy3 = favorite_colors[:]      # Using slicing
print("Cloned color lists:", copy1, copy2, copy3)

# 10. Combine Lists
# Append one list to another
morning_tasks = ['wake up', 'brush teeth']
evening_tasks = ['dinner', 'read book']
all_day_tasks = morning_tasks + evening_tasks
print("Full day task list:", all_day_tasks)

# 11. Sort by Last Element in Tuple
# Sort a list of tuples based on the last element
fruit_weights = [('apple', 120), ('banana', 80), ('cherry', 10)]
sorted_fruits = sorted(fruit_weights, key=lambda x: x[-1])
print("Fruits sorted by weight:", sorted_fruits)

# 12. List Slicing
# Print the first 4 elements from a list
team_members = ["Tunde", "Chika", "Sade", "Emeka", "Ngozi", "Kunle", "Bisi", "Ayo", "Funke", "Obi"]
print("First four team members:", team_members[:4])

# -------------------------
# Part 3: Sets
# -------------------------

# 13. Create a Set
# Sets automatically remove duplicates
programming_languages = {"python", "java", "c++", "javascript", "golang"}
print("Programming languages set:", programming_languages)

# 14. Set Intersection
# Find common elements between two sets
fruit_basket_one = {"apple", "banana", "cherry", "date"}
fruit_basket_two = {"banana", "date", "fig", "grape"}
common_fruits = fruit_basket_one & fruit_basket_two
print("Common fruits:", common_fruits)

# 15. Set Union
# Combine two sets without duplicates
all_fruits = fruit_basket_one | fruit_basket_two
print("Union of fruit baskets:", all_fruits)

# -------------------------
# Part 4: Functions
# -------------------------

# 16. Multiply List Elements
# Function returns product of all numbers in a list
def multiply_factors(number_list):
    product = 1
    for n in number_list:
        product *= n
    return product

numbers_to_multiply = [2, 3, 4]
print("Product of numbers:", multiply_factors(numbers_to_multiply))

# 17. Statistics Function
# Function returns minimum, maximum, and average of a list
exam_scores = [78, 82, 91, 87, 69]
def score_statistics(scores):
    minimum_score = min(scores)
    maximum_score = max(scores)
    average_score = sum(scores) / len(scores)
    return minimum_score, maximum_score, average_score

min_score, max_score, avg_score = score_statistics(exam_scores)
print("Exam score stats -> Min:", min_score, "Max:", max_score, "Average:", avg_score)

# 18. Check Range Membership
# Function checks if a number is within a specified range
def within_bounds(value, lower, upper):
    return lower <= value <= upper

print("Is 12 within 10-20?", within_bounds(12, 10, 20))
print("Is 25 within 10-20?", within_bounds(25, 10, 20))

# 19. Dog Speed Analyzer
# Function finds fastest and slowest dog in a nested list
canine_speeds = [["Greyhound", 45], ["Beagle", 20], ["Whippet", 35], ["Bulldog", 12]]

def canine_race_analyzer(dogs):
    fastest_dog = max(dogs, key=lambda x: x[1])  # Find dog with max speed
    slowest_dog = min(dogs, key=lambda x: x[1])  # Find dog with min speed
    return fastest_dog, slowest_dog

fastest, slowest = canine_race_analyzer(canine_speeds)
print("Fastest dog:", fastest[0], "at", fastest[1], "mph")
print("Slowest dog:", slowest[0], "at", slowest[1], "mph")
