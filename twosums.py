sum1=sum2=0 
num1=int(input("Enter any number:"))
num2=int(input("Enter any number:"))
num3=int(input("Enter any number:"))
sum1=num1+num2+num3
if num1 != num2 and num2!=num3:
    sum2+=num1 
if num2 != num1 and num2!=num3:
    sum2+=num2 
if num3!=num1 and num3!=num2:
    sum2+=num3
print("The numbers are", num1,num2,num3)
print("The sum of three numbers is",sum1)
print("The sum of non duplicate numbers is",sum2)









