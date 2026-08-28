age = int(input("Enter your age: "))

if age >= 18 and age <= 60:
    print("You are eligible")

else:
    print("You are not eligible")


# Discount system :

student = False
senior_citizen = False

if student or senior_citizen:
    print("Discount")
else: 
    print("No discount")