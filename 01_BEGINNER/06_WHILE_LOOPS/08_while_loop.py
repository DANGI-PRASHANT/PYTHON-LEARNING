
while True:

    
    number = input("Enter a number ( or 'stop' to exist): ")

    if number.lower() == "stop":
        break

    num = int(number)

    if num == 1:
        print("Suday")
        print("Today is Holiday")
    elif num == 2:
        print("Monday")
    elif num == 3:
        print("Tuesday")
    elif num == 4:
        print('Wednesday')
    elif num == 5:
        print('Thusday')
    elif num == 6:
        print("Friday")
    elif num == 7:
        print("Saturday")
        print("Today is Holiday")

    else:
        print("ERROR ⚠️")
        break