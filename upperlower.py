str= input("Enter any sentence: ")
uppercount=lowercount=0
alphacount=digitcount=symcount=0
for a in str:
     if a.isupper():
         uppercount+=1
     elif a.islower():
         lowercount+=1
     elif a.isalpha():
         alphacount+=1
     elif a.isdigit():
         digitcount+=1
     elif a.isalnum() != True and a != " ":     #string is not alphanumeric and a blankspace/whitespace
         symcount+=1
print("alphabet count:",uppercount+lowercount)
print("uppercase count:",uppercount)
print("lowercase count:",lowercount)
print("digit count:",digitcount)
print("symbol count:",symcount)                                                                               