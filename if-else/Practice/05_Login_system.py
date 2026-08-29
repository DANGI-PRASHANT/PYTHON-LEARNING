
# simple login system 

username = input("Enter username: ")

if username == "admin":
    password = input("Enter password: ")
    if password == "1234":
        print("Login Successfull")
    else:
        print("Incorrect password.")
else: 
    print("Invalid username")
