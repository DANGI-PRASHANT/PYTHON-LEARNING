# 11. TUPLES PACKING AND UNPACKING (VERY IMPORTANT):

# Tuples packing 
    # putting values into a tuple:

students = ["Ram","24","Nepal"]

# Tuples unpacking:

name , age, country = students
print(name)
print(age)
print(country)

    # A . Another example :

person = ["Ram","25","kathmandu","nepal"]

name_01 , age_01 , city , country_01 = person

print(f"My name is  {name_01}")
print(f"I am {age_01} years old")
print(f"I lived in {city} city")
print(f"I am currently doing business {country_01}")


# B. example:

product = ("Laptop",125000,"4 star")

name_02 , price, rating = product
print(name_02 )
print(price)
print(rating)


# C. Example little different than other (Star):

prices = (12000,11000,10000,9000,8000,7000,60000)

today_price , yesterday_price , *remaining= prices  # remaining take whole collection .
 
print(today_price)
print(yesterday_price)
print(remaining)

