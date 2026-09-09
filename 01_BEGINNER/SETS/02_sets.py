# 3. Characterstic of a set (very important)
    # A. unorder: 

nums = {12,334,56,67,78,23,22,12,21}

print(nums) # output is unorder formed.

    # B. No-indexing:

fruits = {"apple","banana","orange"}
# print(fruits[0])  # EROR....

    # C. No Duplicate item:

nums_01 = {1,2,3,3,4,5,5,6,6,7,7,6}
print(nums_01)

    # D. Fast membership check:

fruits_01 = {"apple","orange","mango"}

print("apple" in fruits) #output is True.

# another example:

name = {"ram","shyam","hari"}

print("sita" in name)  # output is False.


# 4. Accessing set elements:

fruits_02 = {"apple","orange","mango"}

for fruit in fruits_02:
    print(fruit)

# 5. Adding item to a set:

    # A. Add item:

fruits_03 = {"apple","orange","mango"}

fruits_03.add("watermelon")
print(fruits_03)

     #example:

name_01 = {"ram","alex","hari"}

name_01.add("shyam")
print(name_01)

# B. Update(iterable):

device = {"ios","andorid","mobile","computer"}

device.update(["watch","airpods"])
print(device)