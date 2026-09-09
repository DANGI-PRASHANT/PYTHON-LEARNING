# Function with example: 

/
def greet():
    print("Hello guys")
greet()

def mouse ():
    print("The computer")
mouse()


def greet():
    print("Good morning")
greet()


# 1. TYPES OF FUNCTION: 

    # A. with parameters, without return:

def greet(name):
    print(f"Good morning {name}")

greet("Ram")



def hello (name1):
    print(f"Good evening {name1}")
hello(input("Enter your name: "))



def Hi (age):
    print("Eligible" if age>=18 else "Non-eligible")

Hi(int(input("Enter your age: ")))



def info (name,age,location,salary):
    print(f"My name is {name}.I am {age} years old. My location is {location} and My salary is {salary}")
info ("Ram",16,"kathmandu",23000)
info ("shyam",13,"pokhara",12000)


def num (a,b):
    print(f"Add : {a+b}")
    print(f"sub: {a-b}")
    print(f"multi : {a*b}")
    print(f"div : {a/b}")

num (1,3)


    # B.without paratemers,with returns:

def word():
    return "Aeroplane"
print(word())


def name():
    return "prashant"
print(name())

    # C. with parameters and with return:

def add (a,b):
    return a+b
print(add(2,3))

def sub (a,b):
    return a-b
print(sub(2,3))

def multi (a,b):
    return a*b
print(multi(2,3))

def div (a,b):
    return a/b
print(div(2,3))