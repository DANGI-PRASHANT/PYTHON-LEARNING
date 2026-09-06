# 1.single items tuple (very important)

number = (1)

print(type(number)) # it is not tuples , python consider a interger.
print(number) # it is wrong 

# it is a correct :

num = (1,)
print(type(num))
print(num)  # correct



# 2. String and list convert into tuples:

words = "python" #string
fruits = ["apple","banana","pineapple"] # list

result1 = tuple(words)
result2 = tuple(fruits)

print(result1)
print(result2)


# 3. empty tuples:

empty1 = ()
empty2 = tuple()

print(empty1)
print(empty2)

# 4. Accessing tuple elements (indexing)

fruits_01 = ("apple", "banana","mango")
print(fruits_01[0]) # apple
print(fruits_01[1]) # banana
print(fruits_01[2]) # mango


# 5. Negative indexing :

fruits_02 = ["apple","banana","kera"]
print(fruits_02[-1]) # kera
print(fruits_02[-2]) # banana


# 6 . slicing tuples:

nums = (10,20,30,40,50)
print(nums[1:4])  # (20,30,40)
print(num[:3]) # (10,20,30)
print(num[2:]) #(30,40,50)
print(num[::-1]) # reversed tuple 

