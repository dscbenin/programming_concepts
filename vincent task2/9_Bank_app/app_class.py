import datetime as dt
import os
import time
from bankapp import alluser
from bankapp import userdet

now = dt.datetime.now()
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
