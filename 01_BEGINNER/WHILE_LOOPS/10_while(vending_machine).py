# COLD DRINK VENDING MACHINE SIMULATOR: 

want = input("Do you want buy (yes/no): ")
print("            CHOOSE COLD DRINKS          ")
print("""                    🥤 Coke (press 1)
                    🥤 Sprite (press 2)
                    🥤 Fanta (press 3)
                    🥤 Diet Coke (press 4)
                    🥤 Red Bull (press 5)""")
print("         If you want exit, (press 0)         ")
if want.lower() == "yes":


    while True:


        num = int(input("Press a Number: "))
        if num == 1:
            print("     You Got COKE        ")

        elif num == 2:
            print("     You Got Sprite      ")

        elif num == 3 :
            print("     You Got Fanta       ")
        elif num ==4:
            print("     You Got Diet coke       ")
        elif num == 5:
            print("     You Got Red Bull        ")
        elif num == 0:
            print("Thanks")
            print("Exit")
            break
        else:
            print("ERROR ⚠️")
            break
        print()
        
    
        
        
elif want.lower() == "no":
    print("Thanks")
else:
    print("ERROR ⚠️")