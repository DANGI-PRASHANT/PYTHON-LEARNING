# 7. Updating a tuples:

num1 = (1,2,3)
num2 = (4,5,6)

print(num1 + num2)  # output : (1,2,3,4,5,6)

# Another example of tuples:

num3 = (1,2,3,4,5)
num4 = (6,)

print(num3 + num4)

# 8. Removing items: 
# ---> First of convert into list and do update than again convert into tuple:

# numbers = (1,2,3,4,5)

# new_numbers = list(numbers)

# new_numbers.pop()

# number_01 = tuple(new_numbers)
# print(number_01)


#Another examples:

# numbers_01 = (12,23,4,5,6,7)

# new_number_01 = list(numbers_01)

# new_number_01.pop()
# new_numbers_01 = tuple(new_number_01)
# print(new_number_01)


9. # Iterating through in tuples:

fruits = ("apple","banana","mango","orange")

for fruit in fruits:
    print(fruit)


            # lenthing methods: 


for i in range(len(fruits)):
    print(fruits[i])

    # using enumerate :

for index,fruit in enumerate (fruits,1):
    print(f" {index}. {fruit}")

# 10. swiping methods in tuples:

age_ram = 30 
age_shyam = 40

age_ram,age_shyam = age_shyam,age_ram

print(age_ram)
print(age_shyam)


# another simple example:

x = 1
y =3 

x,y = y,x
print(x)
print(y)

