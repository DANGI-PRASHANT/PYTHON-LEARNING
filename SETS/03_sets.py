# 6. Removing item:

# A. Remove:

# fruits = {"apple","orange","mango"}

# fruits.remove("apple")
# print(fruits)

# B. Discard: 

# name = {"ram","shyam","krishna","hari"}

# name.discard("ram")
# print(name) # no error when item is not in list.


# C. pop():

fruits_01 = {"apple","orange","mango"}

removed = fruits_01.pop()
print(fruits_01)
print(f"{removed} deleted")