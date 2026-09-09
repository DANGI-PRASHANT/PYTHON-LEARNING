# Dictionaries Methods:

student = {
    "name" : "Anisha",
    "class" : "Ten",
    "age" : 17,
    "location" : "Tulsipur,Dang"
    
}


print (student.keys()) # key
print(student.values()) # values 
print(student.items()) # items


for key in student:
    print(key)  # Loop through key

for value in student.values():
    print(value) # Loop through value

for key,value in student.items():
    print(f" {key} = {value}")


# 10.Checking key or value in Dictionary:

    student_01 = {
    "name" : "Sita",
    "age" : 17,
    "location" : "Tulsipur,Dang"
    
}



print("name" in student_01) # true
print("grade" in student_01) # false

print("Ram" in student_01.values()) # false
print(17 in student_01.values()) # true