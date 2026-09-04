# BMI CALCULATOR:

while True:


    weight = float(input("Enter a Weight(kg) : "))
    height = float(input("Enter a Height(m): "))


    if weight == "0":
        break

    height1 = height **2
    bmi = weight / height1

    if bmi >=30.0:
        print("Obesity")

    elif bmi >=25.0:
        print("Over Weight")
    elif bmi >= 18.5:
        print("Healthy weight")
    elif bmi <=18.5:
        print("Under-Weight")
    print()
    break
        

    
    
   
