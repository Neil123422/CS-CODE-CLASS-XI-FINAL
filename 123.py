n=int(input("Enter number of rows:"))
for i in range (1,n+1):
 for j in range (1,i+1):
  print(i,end="")
 
 print("\n")  #gives 1 , 22, 333, 4444, 55555


 n = int(input("Enter number of rows: "))

for i in range(1,n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()  # gives 1, 12, 123, 1234, 12345