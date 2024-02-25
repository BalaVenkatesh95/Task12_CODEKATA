# Initialize result string with the first character of input
# Input string
input_str = input()

# Initialize result string with the first character of input
result = input_str[0]

# Iterate over the input string starting from the second character
for i in range(1, len(input_str) - 1):
    # Check if the current character is different from the previous one and the next one
    if input_str[i] != input_str[i - 1] and input_str[i] != input_str[i + 1]:
        # If different, append it to the result string
        result += input_str[i]

# Append the last character of the input string
result += input_str[-1]

# Print the result
if len(result) == 0:
    print(-1)
else:
    print(result)


