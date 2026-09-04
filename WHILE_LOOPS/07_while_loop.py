# Take a number as input in a loop and check if it is positive, negative, or zero (keep asking until
 # user enters 'stop').]


while True:
    value = input("Enter a number (or 'stop' to exit): ")

    if value.lower() == "stop":
        break
    

    num = float(value)

    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")