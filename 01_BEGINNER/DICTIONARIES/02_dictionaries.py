# Changing/ update items:

# ----> changing:

student = {
    "name" : "Sita",
    "class" : "Ten",
    "age" : 17,
    "location" : "Tulsipur,Dang"
    
}

student["name"] = "Anisha" # change
student["age"] = 18 # change
student["country"] = "Neapl" # Add a items.
 
print(student)

# -----> Update:

student.update({"Gender" : "Female" ,"Fee" : 5000})
print(student)  # if data is already here than update otherwise add .


# Removing items:
    #----> pop()

deleted = student.pop("class")
print(f"{deleted} is deleted.")


    # ---> popitem()

student.popitem()
print(student) # deleted last value.

    #-----> clear():

student.clear()
print(student) # output : {}

    #----> del

del student
print(student)