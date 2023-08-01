import math

# initialize the vector
number = [1, 2, 3, 4, 5]

# Access the elements individually
number3 = number[2]
print(f'the third element is {number3}')

# calculate the sum of the vector
sum_of_element = sum(number)
print(f'the sum of the above instantiated vector is {sum_of_element}')

# perform elementwise addition
other_number = [6, 7, 8, 9, 10]
addition_result = [x + y for x, y in zip(number, other_number)]
print(f"the elementwise addition of vector = {addition_result}")

# perform elementwise multiplication
multiplication_result = [x * y for x, y in zip(number, other_number)]
print(f"the elementwise multiplication result is {multiplication_result}")

# find the maximum and minimum values in the vector
max_element = max(number)
min_element = min(number)
print(f"The maximum element is {max_element} and the minimum element is {min_element}")

# Sorting the vectors
sorted_list_asc = sorted(number)
sorted_list_desc = sorted(number, reverse=True)
print(f"The list in ascending order: {sorted_list_asc}")
print(f"The list in descending order: {sorted_list_desc}")


# finding the vector magnitude in the same factor
def vector_magnitude(vector):
    squared_sum = sum([x ** 2 for x in vector])
    magnitude = math.sqrt(squared_sum)
    return magnitude


magnitude_number = vector_magnitude(number)
print(f"The magnitude of the vector 'number' is {magnitude_number}")
