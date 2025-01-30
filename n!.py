def factorial(n):
 if n<0:
  print("negative factorials do not exist")
 elif n==1:
    return 1 
 else:
   result=1
   for i in range (1,n+1):
     result*= i 
 return result 
n=int(input("Enter the number you want the factorial of:"))
print(f"The factorial of {n} is: {factorial(n)}")
  