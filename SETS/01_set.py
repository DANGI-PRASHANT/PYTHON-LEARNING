# How to create sets:

fruits = {"apple","banana","mango"}
nums = {1,2,3,4,5}
friends = {"ram","shyam","krishna","raghav"}
person = {"ram","alex","leo","sam","mariom","gita"}




print(type(fruits))
print(type(nums))
print(friends)
print(type(person))


print(person)
print(fruits)
print(nums)
print(friends)


# Another example and important notes :

#Notes : sets cannot repeat the value. lets see example:

numbers = {1,2,3,4,5,5,6,6}

print(numbers)  # output : {1,2,3,4,5,6}



## 2. Converting list , tuple and string into sets :

word = "apple"

nums_01 = [1,2,3,4,5]

friends = ["ram","shyam","sita"]

result1 = set(word)
result2 = set(nums_01)
result3 = set(friends)

print(result1)
print(result2)
print(result3)

            # Another example tuple convert into sets:

num_01 = 1,2,3,4,5

result = set(nums_01)
print(result)

# 3. create an Empty set:

empty = {}

print(type(empty)) # python not conisder empty set . it consider a empty dictonary . 
print(empty)   # this is wrong way to create empty set.

# Correct way:

empty1 = set()

print(type(empty1))
print(empty1)