from account import Account

if __name__ == '__main__':
    # create an account with the name John Doe
    myAccount = Account("John Doe")

    reply = int(input("What will you like to do " + myAccount.name + " \n1. Deposit\n2. Withdraw: "))
    if reply == 1:
        amount = float(input("Enter the amount you wish to deposit: "))
        myAccount.deposit(amount)
    elif reply == 2:
        amount = float(input("Enter the amount you wish to withdraw: "))
        myAccount.withdrawal(amount)

    print(myAccount.__str__())