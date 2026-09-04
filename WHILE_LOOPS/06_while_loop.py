# Find the sum of digits of a number, then check if the sum is even or odd.


num = int(input("Enter a number: "))

i = 1
sum = 0

while i <=num:
    
    if sum %2 ==0:
        print(f"Even is {sum}")
    else:
        print(f"Odd is {sum}")
    print()

    sum +=i
    i +=1
