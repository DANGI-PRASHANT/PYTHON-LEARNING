# Check if the username is 'admin'.

username = input("Enter an username: ")

password = input("Enter your password: ")

if username == "admin" and password == "1234":
    print("Login Sucessful")
else:
    print("Invalid username or password")