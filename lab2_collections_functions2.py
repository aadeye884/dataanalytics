# -------------------------
# Lab 2: Python Basics – Collections & Functions
# Unique, descriptive, and original naming
# -------------------------

# -------------------------
# Part 1: Tuples
# -------------------------

# 1. Create and Access
speed_factors = (11, 22, 33, 44, 55)
print("Third speed factor:", speed_factors[2])

# 2. Tuple Modification (Workaround)
speed_list = list(speed_factors)
speed_list.remove(33)
adjusted_speeds = tuple(speed_list)
print("Adjusted speeds after removal:", adjusted_speeds)

# 3. Tuple Unpacking
planet_masses = (101, 202, 303, 404, 505)
mercury, venus, earth, mars, jupiter = planet_masses
print("Unpacked planet masses:", mercury, venus, earth, mars, jupiter)

# 4. Tuple to String
greeting_chars = ('H', 'e', 'l', 'l', 'o')
greeting_word = ''.join(greeting_chars)
print("Greeting word:", greeting_word)

# 5. Find Duplicates
lucky_numbers = (7, 14, 7, 21, 28, 14, 35)
repeats_found = set([n for n in lucky_numbers if lucky_numbers.count(n) > 1])
print("Repeated numbers in lucky_numbers:", repeats_found)

# 6. Reverse Tuple
print("Reversed speed factors:", speed_factors[::-1])

# -------------------------
# Part 2: Lists
# -------------------------

# 7. Sum of List
daily_steps = [5000, 7500, 8000, 6200, 7000]
total_steps = sum(daily_steps)
print("Total steps this week:", total_steps)

# 8. Remove Duplicates while keeping order
visited_countries = ['Nigeria', 'Ghana', 'Nigeria', 'Kenya', 'Ghana']
unique_countries = []
for country in visited_countries:
    if country not in unique_countries:
        unique_countries.append(country)
print("Unique countries visited:", unique_countries)

# 9. Clone a List (three ways)
favorite_colors = ['red', 'green', 'blue']
copy1 = favorite_colors.copy()
copy2 = list(favorite_colors)
copy3 = favorite_colors[:]
print("Cloned color lists:", copy1, copy2, copy3)

# 10. Combine Lists
morning_tasks = ['wake up', 'brush teeth']
evening_tasks = ['dinner', 'read book']
all_day_tasks = morning_tasks + evening_tasks
print("Full day task list:", all_day_tasks)

# 11. Sort by Last Element in Tuple
fruit_weights = [('apple', 120), ('banana', 80), ('cherry', 10)]
sorted_fruits = sorted(fruit_weights, key=lambda x: x[-1])
print("Fruits sorted by weight:", sorted_fruits)

# 12. List Slicing
team_members = ["Tunde", "Chika", "Sade", "Emeka", "Ngozi", "Kunle", "Bisi", "Ayo", "Funke", "Obi"]
print("First four team members:", team_members[:4])

# -------------------------
# Part 3: Sets
# -------------------------

# 13. Create a Set
programming_languages = {"python", "java", "c++", "javascript", "golang"}
print("Programming languages set:", programming_languages)

# 14. Set Intersection
fruit_basket_one = {"apple", "banana", "cherry", "date"}
fruit_basket_two = {"banana", "date", "fig", "grape"}
common_fruits = fruit_basket_one & fruit_basket_two
print("Common fruits:", common_fruits)

# 15. Set Union
all_fruits = fruit_basket_one | fruit_basket_two
print("Union of fruit baskets:", all_fruits)

# -------------------------
# Part 4: Functions
# -------------------------

# 16. Multiply List Elements
def multiply_factors(number_list):
    product = 1
    for n in number_list:
        product *= n
    return product

numbers_to_multiply = [2, 3, 4]
print("Product of numbers:", multiply_factors(numbers_to_multiply))

# 17. Statistics Function
exam_scores = [78, 82, 91, 87, 69]

def score_statistics(scores):
    minimum_score = min(scores)
    maximum_score = max(scores)
    average_score = sum(scores) / len(scores)
    return minimum_score, maximum_score, average_score

min_score, max_score, avg_score = score_statistics(exam_scores)
print("Exam score stats -> Min:", min_score, "Max:", max_score, "Average:", avg_score)

# 18. Check Range Membership
def within_bounds(value, lower, upper):
    return lower <= value <= upper

print("Is 12 within 10-20?", within_bounds(12, 10, 20))
print("Is 25 within 10-20?", within_bounds(25, 10, 20))

# 19. Dog Speed Analyzer
canine_speeds = [["Greyhound", 45], ["Beagle", 20], ["Whippet", 35], ["Bulldog", 12]]

def canine_race_analyzer(dogs):
    fastest_dog = max(dogs, key=lambda x: x[1])
    slowest_dog = min(dogs, key=lambda x: x[1])
    return fastest_dog, slowest_dog

fastest, slowest = canine_race_analyzer(canine_speeds)
print("Fastest dog:", fastest[0], "at", fastest[1], "mph")
print("Slowest dog:", slowest[0], "at", slowest[1], "mph")
