# Calculate the sum of numbers from 1 to N (take N as input)


num = int(input("Enter a number: "))

i = 1 
sum = 0

while i <=num:
    sum +=i
    i +=1 

    print(f"Sum: {sum}")