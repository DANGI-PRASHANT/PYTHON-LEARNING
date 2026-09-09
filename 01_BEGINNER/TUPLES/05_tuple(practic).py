#1. Store a tuple data = (10 20 30 40) and print element at index 2.

data = (10,20,30,40)

print(data[2])

# 2. Create a tuple values = (5 10 15 20) and print its length.

values = [5,10,15,20]

print(len(values))


# 3. Create a tuple numbers = (10 20 30 40) and print elements from index 1 to 3 using slicing.

numbers = (10,20,30,40)

print(numbers[1:4])

# 4. Create a tuple nums = (1 2 3) and repeat it 3 times then print.

nums = (1,2,3)

for num in range(3):
    print(nums)


# 5. Store a tuple values = (2 4 6 8) and find maximum and minimum value.

values_01 = (2,4,6,8)

print(max(values_01))
print(min(values_01))


# 6. Create a tuple nums = (5 3 1 4 2) and sort it by converting into list.

nums_01 = (5,3, 1, 4 ,2)

new_nums_01 = list(nums_01)
new_nums_01.sort()
number = tuple(new_nums_01)
print(number)

# 7. Store two tuples a = (1 2 3) b = (4 5 6) and join them into one tuple.

a = (1,2,3)
b = (4,5,6)

print(a + b)

