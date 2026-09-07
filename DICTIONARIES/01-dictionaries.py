# 1.How to create a  dictionaries with example:

    # A. using curl brackets: 

student = {
    "Name" : "Anisha",
    "Grade" : 12,
    "Age" : 17,
    "Country" : "Nepal",
    "City" : "tulsipur"
}

print(student)

# Example:

youtube = {
    "title" : "How to learn python",
    "views" : 5000,
    "likes" : 240

}

print(youtube)


    # B. Using the dict() constructor:

student_01 = dict(name = "ram",age = 24,lccation = "nepal")
print(student_01)

    # C. Empty dictionaries:
empty = {}
empty1 = dict()

print(empty)
print(empty1)


# 2. CHARACTERISTIC OF DICTIONARIES:

# Accessing item:

student_02 = {
    "name" : "Anisha",
    "class" : "Ten",
    "age" : 17,
    "location" : "Tulsipur,Dang"
    
}

print(student_02["name"])
print(student_02["class"])
print(student_02["age"])
print(student_02["location"])


# using get()(safer):

print(student_02.get("name"))
print(student_02.get("age"))
print(student_02.get("city" ,"city not found")) 


# Add New items:

student_02["country"] = "Nepal"
student_02["subject"] = "science"

print(student_02)