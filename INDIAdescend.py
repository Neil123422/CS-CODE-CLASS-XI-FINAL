def print_india_pattern():
    word = "INDIA"
    length = len(word)

    for i in range(length, 0, -1):  # Loop from length to 1
        print(word[:i])  # Print the substring of 'word' from 0 to i

# Call the function to print the pattern
print_india_pattern() 