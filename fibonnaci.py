def fibonnaci_series(n):
 a,b= 0,1
 print("Fibonnaci series:")
 for i in range (n):
  print(a,end="")
  a,b=b,a+b
terms= int(input("Enter the number of terms till which you want to print the fibonnaci series:"))
fibonnaci_series(terms) 

