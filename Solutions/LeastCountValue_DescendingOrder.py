# Get the size of the array from the user
size = int(input())

# Get the values for the array from the user
values = list(map(int, input().split()))

# Count the occurrences of each element
#Using dictionary to store it in key,value pair
counts = {}
for value in values:
    counts[value] = counts.get(value, 0) + 1
'''
.get(value, 0): This method retrieves the value associated with the specified key (value) in the dictionary. 
If the key exists in the dictionary, it returns the corresponding value. 
If the key does not exist, it returns the default value specified as the second argument (0 in this case).
+ 1: After retrieving the value from the dictionary using get(), + 1 increments the value by 1.

'''
# Find the least occurring elements
least_occurrences = min(counts.values())

# Find the elements with the least occurrences
least_occurrence_elements = []
for key, value in counts.items():
    if value == least_occurrences:
        least_occurrence_elements.append(key)

# Sort the least occurring elements in decreasing order
least_occurrence_elements.sort(reverse=True)
print(" ".join(map(str, least_occurrence_elements)))

'''
.get(value, 0): This method retrieves the value associated with the specified key (value) in the dictionary. 
If the key exists in the dictionary, it returns the corresponding value. 
If the key does not exist, it returns the default value specified as the second argument (0 in this case).
+ 1: After retrieving the value from the dictionary using get(), + 1 increments the value by 1.

'''


