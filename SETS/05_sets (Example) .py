# 1.Create a set numbers = {1 2 3 4 5} and print it.

numbers = {1,2,3,4,5}
print(numbers)


# 2.Create a set data = {1 2 2 3 3 4} and print it and observe duplicates removed.

data = {1,2,2,3,3,4}
print(data)

# 3. Store a set fruits = {apple banana mango} and add orange to it then print.

fruits = {"apple","banana","mango"}
fruits.add("orange")
print(fruits)


# 4. Create a set nums = {10 20 30} and update it by adding multiple values 40 and 50.

nums = {10,20,30}
nums.update({40,50})
print(nums)

# 5. Store a set values = {1 2 3 4} and remove element 3 then print the set.

values = {1,2,3,4}
values.remove(3)
print(values)

# 6. Create a set items = {pen pencil eraser} and remove last element using pop and print it

items = {"pen","pencil","eraser"}
items.pop()
print(items)


# 7. Store a set nums = {5 10 15 20} and check if 10 exists in it.

nums_01 = {5,10,15,20}

if 10 in nums_01:
    print("Yes")

# 8. Create two sets a = {1 2 3} b = {3 4 5} and find their union

a = {1,2,3}
b = {3,4,5}

print(a | b)

# 9. Create two sets a = {1 2 3} b = {3 4 5} and find their intersection.

aa = {1,2,3}
bb = {3,4,5}

print(aa.intersection(bb))


# 10. Create two sets a = {1 2 3} b = {3 4 5} and find elements present only in a.

print(a.difference(b))

# 11. Store a set numbers = {1 2 3 4 5} and clear all elements from it.

number = {1,2,3,4,5}
number.clear()
print(number)

# 12. Create a set nums = {10 20 30 40} and print its length.

num = {10,20,30,40}
print(len(num))

