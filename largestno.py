# Input 10 numbers from the user
numbers = list(map(int, input("Enter 10 numbers separated by space: ").split()))

# Ensure exactly 10 numbers are entered
if len(numbers) != 10:
    print("Error: You must enter exactly 10 numbers.")
else:
    # Sort the list in descending order
    numbers.sort(reverse=True)
    
    # Print the third largest number
    print("The third largest number is:", numbers[2])