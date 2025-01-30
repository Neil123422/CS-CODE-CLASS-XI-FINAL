# Input lists from the user
L = list(map(int, input("Enter elements of first list separated by space: ").split()))
M = list(map(int, input("Enter elements of second list separated by space: ").split()))

# Ensure both lists have the same length
if len(L) != len(M):
    print("Error: Lists must be of the same size.")
else:
    # Create the new list by summing corresponding elements
    N = [L[i] + M[i] for i in range(len(L))]
    
    # Print the resulting list
    print("The new list after adding corresponding elements:", N)