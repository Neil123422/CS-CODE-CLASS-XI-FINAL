# Input values of x and n
x = int(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))

# Initialize sum and series string
sum_series = 0
series = ""

# Compute the series and sum
for i in range(n + 1):
    term = (-1) ** i * (x ** i)  # Compute each term
    sum_series += term  # Add to sum
    
    # Format the series
    if i == 0:
        series += "1"
    else:
        series += f" {'-' if i % 2 == 1 else '+'} {x}^{i}"

# Print the series and sum
print("Series:", series)
print("Sum of the series:", sum_series)