# 1. Create a function greet() that prints “Hello, World!” and call it.

def greet():
    print("hello world")
greet()

# 2. Create a function add() that takes two numbers as parameters and prints their sum.
 
def add(a,b):
    print(f"Sum of two number: {a+b}")
add(2,3)

# 3. Create a function multiply(a, b) that returns the product of two numbers and print the result.

def multiply(a,b):
    print(f"multiply of two number: {a*b}")
multiply(5,6)

# 4. Write a function square(n) that returns the square of a number and call it for 5.

def square(a):
    return a*a
print(square(5))

# 5. Create a function is_even(n) that returns True if a number is even, otherwise False

def even_odd(a):
    if a %2==0:
        print("even")
    else:
        print("odd")
even_odd(int(input("Enter a number: ")))


# 6. Write a function greet_name(name) that prints “Hello, name” using the given parameter.

def greet_name(name):
    print(name)
greet_name("Hello")

# 7.Create a function calculate_area(length, width) that returns area of a rectangle.

def calculate_area (length,width):
    return length * width
print(calculate_area(233,344))


#8. Write a function largest(a, b, c) that returns the largest of three numbers.

def largest(a,b,c):
    return a>b>c
print(largest(a = 3,c=6,b=1))


# 9.Write a function sum_list(lst) that returns the sum of all numbers in a list.

def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

nums = [1,2,3,4,5]
print(sum_numbers(*nums))  # 10