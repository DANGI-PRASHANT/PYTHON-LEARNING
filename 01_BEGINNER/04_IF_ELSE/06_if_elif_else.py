# Grada system

marks = int(input("Enter your marks: "))

if marks >=90:
    print("you got A+")
elif marks >=80:
    print("you got A")
elif marks >=70:
    print("You got B+")
elif marks >=60:
    print("You got B")
elif marks >50:
    print("You got C+")
elif marks >=40:
    print("You got C")
else:
    print("Failed")


# Check temperature:

temp = int(input("Enter the temperature: "))

if temp >=35:
    print("Hot")
elif temp >=20:
    print("warm")
elif temp >=10:
    print("cool")
else:
    print("cold")


# Age seperation: 

age = int(input("Enter age: "))

if age >=60:
    print("senior citizer")
elif age >=18:
    print("adult")
elif age >=10:
    print("teenager")
else:
    print("child")
