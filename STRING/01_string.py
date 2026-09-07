# Create a simple string with example:

name = "Prashant"
age = 23
location = "Nepal"

print(name)
print(age)
print(location)

# 2. Accessing characters(indexing)

text = "python"

print(text[0])
print(text[1])
print(text[4])

        # Negative indexing:

print(text[-1])
print(text[-3])

# 3. String slicing:

text = "python"

print(text[1:4]) # yth
print(text[:3]) # pyt
print(text[2:]) # thon
print(text[::-1]) # nohtyp

# 4. String Are immutable:

word = "apple"
# word[1] = "a" #Error

# you can create a new string instead:

word = "a" + word[1:]
print(word)

