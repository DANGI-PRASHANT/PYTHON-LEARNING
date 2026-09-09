# 5. PARAMETERS/ ARGUMENTS:

def sub(a,b):
    print(a-b)

sub(2,3) # positional arugments , order matters.


def info (name,age,location):
    print(f"My name is {age} , age is {age} and location is {location}")

info(age=17,name="prashant",location="ktm") # non-positional arugments,order not matter.


def greet (name = "jhon"):  # Default Arugments system very useful.
    print(f"Good morning {name}")

greet("Ram")
greet("Gita")
greet()


def nums(*numbers):
    print(numbers)

nums(1,2,3,4,5)


# Find sum:

def find_sum(*nums):
    total = 0

    for num in nums:
        total += num
    return(total)

print(find_sum(1,2,3,4,5,6,7,8,9,0))

# Find product:

def product(*nums_01):

    total =1 
    for num_1 in nums_01:
        total *= num_1

    return total
print(product(1,2,3,4,5,6))


# keyword arugments:

def find_info(** info):
    print(info)

find_info(name="Ram",grade=12, location="ktm")


# Another example: 


def product_info(**product):
    for key,value in product.items():
        print(f"{key}: {value}")
product_info(name="Mobile",price=230000,color="black")



# 6. special variables: 

    # local variables: 

def greet():
    product = "clothes"
    print(product)

greet()


    # Global Variable:

name = "Ram"

def greet():
    print(name)
greet()