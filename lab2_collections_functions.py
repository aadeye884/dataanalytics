# Lab 2: Python Basics – Working with Collections and Functions

# -------------------------
# Part 1: Tuples
# -------------------------

# 1. Create and Access
# a. Define a tuple with at least 5 numerical values
num_tuple = (10, 20, 30, 40, 50)

# b. Print the third item in the tuple
print("Third item in tuple:", num_tuple[2])

# 2. Tuple Modification (Workaround)
# Tuples are immutable, so convert to list, modify, then convert back
temp_list = list(num_tuple)  # Convert to list
temp_list.remove(30)         # Remove the value 30
num_tuple_modified = tuple(temp_list)  # Convert back to tuple
print("Tuple after removing 30:", num_tuple_modified)

# 3. Tuple Unpacking
a, b, c, d, e = (1, 2, 3, 4, 5)
print("Unpacked values:", a, b, c, d, e)

# 4. Tuple to String
char_tuple = ('H', 'e', 'l', 'l', 'o')
string_from_tuple = ''.join(char_tuple)  # Join characters into a string
print("String from tuple:", string_from_tuple)

# 5. Find Duplicates
dup_tuple = (1, 2, 2, 3, 4, 4, 5)
duplicates = set([x for x in dup_tuple if dup_tuple.count(x) > 1])
print("Duplicate values:", duplicates)

# 6. Reverse Tuple
print("Reversed tuple:", num_tuple[::-1])

# -------------------------
# Part 2: Lists
# -------------------------

# 7. Sum of List
num_list = [1, 2, 3, 4, 5]
print("Sum of list:", sum(num_list))

# 8. Remove Duplicates (maintain order)
dup_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []
for item in dup_list:
    if item not in unique_list:
        unique_list.append(item)
print("List after removing duplicates:", unique_list)

# 9. Clone a List (three ways)
original_list = [1, 2, 3]
clone1 = original_list.copy()
clone2 = list(original_list)
clone3 = original_list[:]
print("Clones:", clone1, clone2, clone3)

# 10. Combine Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print("Combined list:", list1)

# 11. Sort by Last Element in Tuple
tuple_list = [(1, 2), (3, 1), (5, 0)]
sorted_list = sorted(tuple_list, key=lambda x: x[-1])
print("Sorted by last element:", sorted_list)

# 12. List Slicing
names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack"]
print("First 4 names:", names[:4])

# -------------------------
# Part 3: Sets
# -------------------------

# 13. Create a Set
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)

# 14. Set Intersection
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
intersection = set_a & set_b
print("Intersection:", intersection)

# 15. Set Union
union = set_a | set_b
print("Union:", union)

# -------------------------
# Part 4: Functions
# -------------------------

# 16. Multiply List Elements
def multiply_list(lst):
    product = 1
    for num in lst:
        product *= num
    return product

numbers = [1, 2, 3, 4]
print("Product of list elements:", multiply_list(numbers))

# 17. Statistics Function
import statistics

test_scores = [88, 92, 79, 95, 85]

def get_stats(scores):
    minimum = min(scores)
    maximum = max(scores)
    average = sum(scores) / len(scores)
    return minimum, maximum, average

min_score, max_score, avg_score = get_stats(test_scores)
print("Min:", min_score, "Max:", max_score, "Average:", avg_score)

# 18. Check Range Membership
def is_in_range(number, start, end):
    return start <= number <= end

print("Is 5 in range 1-10?", is_in_range(5, 1, 10))
print("Is 15 in range 1-10?", is_in_range(15, 1, 10))

# 19. Dog Speed Analyzer
dogs = [["Greyhound", 45], ["Beagle", 20], ["Whippet", 35], ["Bulldog", 12]]

def dog_speed_analyzer(dog_list):
    fastest = max(dog_list, key=lambda x: x[1])
    slowest = min(dog_list, key=lambda x: x[1])
    return fastest, slowest

fastest_dog, slowest_dog = dog_speed_analyzer(dogs)
print("Fastest dog:", fastest_dog[0], "at", fastest_dog[1], "mph")
print("Slowest dog:", slowest_dog[0], "at", slowest_dog[1], "mph")
