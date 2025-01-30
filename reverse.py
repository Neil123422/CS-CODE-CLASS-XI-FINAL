str= input("Enter any string: ")
length= len(str)
print("The string", str, "in reverse order is: ")
for a in range (-1,(-length-1),-1):
    print(str[a],end="")
