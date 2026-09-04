
print("                                               WELCOME BANK OF NEPAL                                                          ")

card = True
Balance = 1000
pin = int(input("Enter PIN: "))
select = input("""Select Transaction Type:(Balance /Withdraw / Transfer): """)

if pin == 11:
  

    if  select.lower() == "balance":
        print(f"Your Account Balance is ${Balance}")


    elif select.lower() == "withdraw":

        withdraw_amount = int(input("Enter a withdraw_amount: "))

        if withdraw_amount <=Balance:
            print(f"Withdraw succesfull ${ withdraw_amount}")
            print(f"Remaining Balance is $11{Balance - withdraw_amount}")
        else:
            print("Insufficient Balance")

    elif select.lower() == "transfer":


        check = input("Is sender Balance sufficient? (yes/No): ")

        if check == "yes":

            Recipit_number = str(input("Enter a Recipient Account or Debit card Number: "))
            amount = float(input("Enter Amount to Transfer: "))
            
            verify = input("(confrim / Denied):")

            if verify == "confrim":
                print(f"Transfer Successfull")
                print(f"Remaining amount is ${Balance - amount}")
            else:
                print("Cancelled Process")
        else:
            print("Insufficient Balance")
else:
    print("Incorrect PIN")

print("                                          THANK YOU !!                                              ")
       

