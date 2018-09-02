#MY_BANK_App: Just open and run!!
#please deposit a certain amount first, so you can get a clear picture of what it does

import datetime
from os import system, name

date = datetime.datetime.now()

bankdata = dict()

class myAccount:

    first_name = "Osita"
    middle_name = "Excel"
    last_name = "Edagwa"
    user_name = "excelkid"
    password = "namikaze"
    start_balance = 1000000
    account_id = 10010000

    def __init__(self):
        self.start_balance = 0

    def create_Account(self):
        self.first_name = input("input your firstname: ")
        self.middle_name = input("input your middlename: ")
        self.last_name = input("input your lastname: ")
        self.user_name = input("input your username: ")
        self.password = input("input your password: ")
        self.account_id += 100
        data = self.password
        bankdata[self.password] = [self.password]
        print("Your account username is: ", self.user_name)
        print("Your account id is", self.account_id)

    def check_Balance(self):
        print("Transaction Initialized @", date)
        print("Your Current Balance is: ", float(self.start_balance))



    def Deposit_Money(self):
        i = int(input("Please input the amount you'll like to deposit: "))
        self.start_balance += i
        print("Transaction Successful!, Your new balance is: ", float(self.start_balance))
        print("Transaction Complete @", date)

    def Transfer(self):
        i = int(input('Please enter the amount you would like to transfer: '))
        if i >= self.start_balance:
            print('Sorry, you currently have insufficient balance to peform this transaction')
        elif i > 0 <= self.start_balance:
            self.start_balance -= i
            print('Transaction Successful @', date)
            print('Your new balance is: ', float(self.start_balance))

    def Withdrawal(self):
        i = int(input('Enter the amount you want to withdraw: '))
        if i >= self.start_balance:
            print('Sorry, you currently have insufficient balance to peform this transaction')
        elif i > 0 <= self.start_balance:
            self.start_balance -= i
            print('Transaction Successful @', date)
            print('Your new balance is: ', float(self.start_balance))

def pause_screen():
    print("<<<<<<Press Enter to continue>>>>>>")
    input()

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def App_menu():
    clear()
    print()
    print("<<<<<<**MY BANK APP: MENU**>>>>>>")
    menu_list = ['Create Account', 'Deposit', 'Check Balance', 'Withdrawal','Transfer', 'Exit']
    for i, menu_list in enumerate(menu_list, start=1):
        print(i, menu_list)
    ex=int(input("Choose a preferred option: "))
    return ex



bank = myAccount()



while True:

    ex = App_menu()

    if ex == 1:
        print()
        print()
        ex = bank.create_Account()
        print('Congratulations, Your Account has been created successfully! @', date)
        pause_screen()
        continue


    elif ex == 2:
        clear()
        print()
        i = input("Please enter your password: ")
        if i in bankdata:
            ex = bank.Deposit_Money()
        else:
            print ("Sorry, this does not match any password in our database, please input a valid password")
        pause_screen()
        continue


    elif ex == 3:
        clear()
        print()
        i = input("Please enter your password: ")
        if i in bankdata:
            ex = bank.check_Balance()
        else:
            print ("Sorry, this does not match any password in our database, please input a valid password")
        pause_screen()
        continue


    elif ex == 4:
        clear()
        print()
        i = input("Please enter your password: ")
        if i in bankdata:
            ex = bank.Withdrawal()
        else:
            print ("Sorry, this does not match any password in our database, please input a valid password")
        pause_screen()
        continue

    elif ex == 5:
        clear()
        print()
        i = input("Please enter your password: ")
        if i in bankdata:
            ex = bank.Transfer()
        else:
            print ("Sorry, this does not match any password in our database, please input a valid password")
        pause_screen()
        continue

    elif ex == 6:
        clear()
        print()
        print("****Thank You for banking with us!****")
        break

    else:
        clear()
        print()
        App_menu()
        continue







