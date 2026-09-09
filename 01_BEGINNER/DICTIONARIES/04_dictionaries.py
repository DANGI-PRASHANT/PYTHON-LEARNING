# nested Dictionaries with example :

student = {
    "name" : "anisha",
    "age" : 17,
    "grade" : 12,
    "location" : "tulsipur",
}

student_info = { 
    "student_1" : {"name" : "anisha" , "age" : 17, "grade" : 12 , "location" : "tulsipur"},
    "student_2" : {"name" : "ram" , "age" : 12,"grade" : 7, "location" : "Dang"},
    "student_3" : {"name" : "hari" , "age" : 23 , "grade" : 12 , "location" : "ktm"}

}

print(student_info["student_1"]["name"])
print(student_info["student_3"]["location"])



# Another example of Nested Dictionaries: 



Gadget = {
    "name" : "Mobile",
    "series" : "1234qwerty",
    "Storage" : "256 GB",
    "Ram" : "16 Gb",
}


Gadget_info = {

    "Gadget_1" : {"name" : "Mobile", "series" : "12345qwert","storage" : "256 gb", "Ram" : '16 gb'},
    "Gadget_2" : {"name": "laptop","series": "8984dskf", "storage": "1 tb", 'ram': "16 gb"},
    "Gadget_3" : {"name": "watch","series": "123klkds","storage": "56GB","ram" : "8 GB"},

}

print(Gadget_info["Gadget_1"]["name"])
print(Gadget_info["Gadget_2"]["series"])
print(Gadget_info["Gadget_3"]["storage"])


# Dictionary comprehension:

nums = {x:x **2 for x in range(1,7)}
print(nums)

num_1 = { i:i+1 for i in range(1,10)}
print(num_1)

num_2 = {a : a-1 for a in range(1,8)}
print(num_2)