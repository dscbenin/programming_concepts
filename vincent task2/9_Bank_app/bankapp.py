import datetime as dt
import os
import time
import app_class
import app_function

now = dt.datetime.now()
alluser = list()
userdet = dict()

class Account:
    sex = "M"
    name = "Akinwande gbenga vincent"
    age = 19
    time = now.strftime("%Y-%m-%d %H:%M")
    Balance = 2000000000
    Password = 20122013
    id = 0

    def __init__(self):
        self.Balance = 0

    def CreateAccount(self,ID):
        self.name = input("Enter name: ")
        self.Password = input("Enter Password: ")
        self.age = int(input("Enter age: "))
        self.sex = input("[M/F]: ")
        self.id = ID
        userdet[self.id] = [self.name,self.Password]
        print("Your ID is: ",self.id)
        print("Account Successfully Created @ ",self.time)
        
    def Check_Balance(self):
        print("Account Balance: ",self.Balance)

    def Deposit(self):
        new = int(input("How much will you like to deposit?: "))
        self.Balance += new

    def Transfer_to(self,to):
        amount = int(input("amount: "))
        if amount > self.Balance:
            print("Insuficient Balance")
        elif self.id == to:
            print("you can't transfer to userself")
        else:
            alluser[to].Balance = amount

    def Withdraw(self):
        amount = int(input("amount: "))
        self.Balance -= amount

def displayoption():
    os.system("clear")
    print("************ SELECT OPERATION **************\n")
    print("[1] Create Account ")
    print("[2] Check Balance")
    print("[3] Deposit")
    print("[4] Withdraw")
    print("[5] Transfer")
    print("[0] Exit\n")
    reply = int(input("Enter input: "))
    return reply

def clear():
    os.system("clear")

def pause():
    print("<Press Enter to continue>....")
    input()

index = 0

while True:
    reply = displayoption()
    
    if int(reply) == 0:  break

    elif reply == 1:
        alluser.append(index)
        alluser[index] = Account()
        alluser[index].CreateAccount(index)
        print("current users = ",index+1)
        index += 1 
        pause()
        continue

    elif reply == 2:
        clear()
        id = int(input("Enter Id: "))
        if id in userdet:
            name = input("Enter name: ")
            password = input("Password: ")
        else:
            print("Invalid Id...")
            pause()
            continue

        if name == alluser[id].name and password == alluser[id].Password:
            clear()
            alluser[id].Check_Balance()
        pause()
        continue
    
    elif reply == 3:
        clear()
        id = int(input("Enter Id: "))
        if id in userdet:
            name = input("Enter name: ")
            password = input("Password: ")
        else:
            print("Invalid Id...")
            pause()
            continue

        if name == alluser[id].name and password == alluser[id].Password:
            clear()
            alluser[id].Deposit()
        pause()
        continue

    elif reply == 4:
        clear()
        id = int(input("Enter Id: "))
        if id in userdet:
            name = input("Enter name: ")
            password = input("Password: ")

        else:
            print("Invalid Id...")
            pause()
            continue

        if name == alluser[id].name and password == alluser[id].Password:
            clear()
            alluser[id].Withdraw()
        pause()
        continue
        
    
    elif reply == 5:
        clear()
        id = int(input("Enter Id: "))
        if id in userdet:
            name = input("Enter name: ")
            password = input("Password: ")
        else:
            print("Invalid Id...")
            pause()
            continue

        if name == alluser[id].name and password == alluser[id].Password:
            clear()
            trans_to = int(input("Transfer to: "))
            if trans_to in userdet:
                alluser[id].Transfer_to(trans_to)
            else:
                print("invalid Id...")
                pause()
                continue
        pause()
        continue
    else:
        displayoption()
        continue