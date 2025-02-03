print("Enter 5 numbers below")
num1=float(input("Enter any number:"))
num2=float(input("Enter any number:"))
num3=float(input("Enter any number:"))
num4=float(input("Enter any number:"))
num5=float(input("Enter any number:"))
divisor=float(input("Enter divisor:"))
count=0 
print(f"Multiples of {divisor} are")
remainder= num1%divisor
if remainder==0:
    print(num1,sep="")
    count+=1 
    remainder=num2%divisor
if remainder==0:
    print(num2,sep="")
count+=1 
remainder=num3%divisor
if remainder==0:
    print(num3,sep="")
count+=1 
remainder=num4%divisor
if remainder==0:
    print(num4,sep="")
count+=1 
remainder=num5%divisor
if remainder==0:
    print(num5,sep="")
count+=1 
print()
print(f"Total multiples of {divisor} are {count}")