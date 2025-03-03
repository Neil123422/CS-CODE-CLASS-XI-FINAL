radius= float(input("Enter radius of the circle:"))
print("1. Calculate Area")
print("2. Calculate perimeter")
choice= int(input("Enter your choice(1 or 2):"))
if choice==1:
    area= 3.14*radius**2
    print(f"Area of the circle is {area}")
else:
    perimeter= 2*3.14*radius
    print(f"Perimeter of the circle is {perimeter}")    