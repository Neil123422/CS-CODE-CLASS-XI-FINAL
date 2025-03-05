# to print x, x^2, x^3, x^4, x^5...x^n
x= int(input("Enter any number: "))
n= int(input("Enter highest power:"))
sum= 0 
if x<x*n:
    for i in range(1,n+1):
        sum+=x**i
        print(x**i, end=", ")
    print("\nSum of the series is:", sum)