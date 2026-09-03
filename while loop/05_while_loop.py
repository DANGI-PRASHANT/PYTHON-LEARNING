# . Print numbers from 1 to 20, printing 'Even' or 'Odd' next to each number.

i = 1 

while i <=20:
    if i %2 ==0:
        print(f"Even: {i}")
    else:
        print(f"Odd: {i}")
    print()
    i +=1