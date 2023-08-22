# function to calculate the Hamming distance between the two strings

def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Input strings must have the same length")

    distance = 0
    for bit1, bit2 in zip(str1, str2):
        if bit1 != bit2:
            distance += 1
    return distance


# function for comparing binary strings

def compare_binary_strings(str1, str2):
    distance = hamming_distance(str1, str2)
    print(f"Hamming Distance between {str1} and {str2}: {distance}")


# function for similarity searches

def similarity_search(target_str, data):
    results = []

    for binary_str in data:
        distance = hamming_distance(target_str, binary_str)
        results.append((binary_str, distance))

    results.sort(key=lambda x: x[1])  # Sort the results  based on Hamming distance
    return results


# Example data
data = ["10111", "11001", "10010", "01100", "11111"]

# Compare the binary strings
compare_binary_strings("10111", "10010")

# Perform Similarity Search
target_str = "10010"
search_results = similarity_search(target_str, data)

# print search results
print("Similarity search Results:")
for result in search_results:
    print(f"Binary Sting: {result[0]}, Hamming Distance: {result[1]}")