from account import Account

if __name__ == '__main__':
    # create an account with the name John Doe
    myAccount = Account("John Doe")

    while True:
        reply = int(input("What will you like to do " + myAccount.name + " \n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit: \n"))
        if reply == 1:
            amount = float(input("Enter the amount you wish to deposit: "))
            myAccount.deposit(amount)
            print("Transaction Succesful")
        elif reply == 2:
            amount = float(input("Enter the amount you wish to withdraw: "))
            myAccount.withdrawal(amount)
            print("Transaction Succesful")
        elif reply == 3:
             print(myAccount.__str__() + "\n")
        elif reply == 4:
            break
        else:
            print("\ninvalid choice, please try again\n")

   
