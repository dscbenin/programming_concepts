"""All in one page. Catches errors, uses sleep, strictly for demo as there's no
external save(d) files(e.g, for storing usernames and passkeys)"""

import os
import sys
from time import sleep
import datetime

class BankAccount():
    print ("Welcome to the Charity Bank. We take our customers very seriously")
    sleep(2)
    print("We've even gone our way to credit your account with #40000.00. You're Welcome")
    sleep(2)
    print ("Kindly slot in your Card to begin transaction.")
    def __init__(self):
        self.name="Demo Customer 007"
        self.bal=40000.00
        self.acc=1
        self.time=datetime.datetime.now().strftime("%d-%B-%Y %H:%M")
        
    def __str__(self):
        print("Account name is {0}\nAccount Balance is {1}, as at {2}".format(self.name, self.bal, self.time))
        print("We currently have {} account(s) on this platform".format(self.acc))
        
    def createAcct(self):
        self.acc+=1
        self.bal=0.00
        self.name=input("Enter Name: ")
        self.bal=float(input("Enter New Account Balance: "))
        print("Done. Account Created")
        return self.newTransact()
    
    def withdrawal(self):
        print("Enter Amount to Withdraw: ")
        try:
            amount=float(input("#"))
        except Exception:
            print("INVALID FORMAT. ONLY NUMBERS ALLOWED")
            self.withdrawal()
        
        if amount <= 0 :
            print("Withdrawal above #0.00 only, please")
            self.withdrawal()
        elif (amount > self.bal):
            print("INSUFFICIENT FUND FOR THIS TRANSACTION. YOU HAVE {} IN YOUR ACCOUNT, ONLY".format(str(self.bal)))
            self.newTransact()
        else:
            print("Your Account has been successfully updated.")
            self.bal-=amount
            sleep(1)
            self.__str__()
            self.newTransact()

            
    def deposit(self):
        print("How much would you like to deposit?")
        try:
            amount=float(input("#"))
        except Exception:
            print("INVALID FORMAT. USE NUMBERS ONLY")
            self.deposit()
            
        if (amount <= 0):
            print("Deposits above #0.00 only, please")
            self.newTransact()
        else:
            print("Your account has been successfully updated")
            self.bal+=amount
            sleep(1)
            self.__str__()
        self.newTransact()
            
    def inquiry(self):
        print("Checking your account. Please wait")
        sleep(2.5)
        self.__str__()
        sleep(1)
        self.newTransact()
        
        return
        
    def transactionMsg(self):
        print ("\nWelcome, valued customer ")
        print (" 1. Create New Account\n 2. Withdrawal\n 3. Deposit\n 4. Inquiry\n 5. Transfer\n 6. quickteller\n 7. exit")
        sleep(1)
        try:
            choice=int(input("Enter your option here: "))
        except Exception:
            print("INVALID INPUT\n\n\nRELOADING OPTIONS, AGAIN\n")
            print("___"*20)
            sleep(1)
            self.transactionMsg()
            
        if (choice == 1):
            self.createAcct()
        elif (choice ==2):
            self.withdrawal()
        elif (choice ==3):
            self.deposit()
        elif (choice==4):
            self.inquiry()
        elif (choice==5):
            print("OPTION NOT AVAILABLE")
            self.transactionMsg()
            
        elif(choice==6):
            self.quickteller()
            sleep(.5) 
        elif(choice==7):
            self.exitMsg()
        else:
            print("OUT OF BOUND. PLEASE USE ONLY VALUES FROM 1-5.")
            self.transactionMsg()
            
    def quickteller(self):
        try:
            pNumber=int(input("Enter your phone number to get recharge card: 0"))
        except Exception:
            print("WRONG FORMAT. ONLY NUMBERS ALLOWED")
            self.quickteller()
            
        if (len(str(pNumber)) == 10 ):
            print("Confirming number is 11 digits")
            sleep(3)
            print("Phone Number is ok")
            try:
                amount=float(input("Universal network initialized. How much would you like to top up? "))
            except Exception:
                print("NUMBERS ONLY.\nGOING BACK")
                sleep(1)
                self.quickteller()
            
            if(amount>self.bal):
                print("INSUFFICIENT FUNDS FOR THIS TRANSACTION. YOU HAVE {} ON YOUR ACCOUNT ONLY".format(self.bal))
                self.newTransact()
            else:
                print("TOPPING UP..........")
                sleep(2)
                print("Done")
                self.bal-=amount
                self.__str__()
                self.newTransact()
            
          
        else:
            print("Number not complete. It must be 11 digits")
            self.quickteller()
        return
            
            
    def newTransact(self):
        choice=input("Would you like to do another transaction? (y/n)").lower()
            
        if (choice=="y") or (choice=="yes"):
            self.transactionMsg()
        elif (choice=="n") or (choice=="no"):
            print("Take Your Card.\nIt's been a pleasure serving you, "+self.name)
            sys.exit(1)
        else:
            print("OPTION NOT RECOGNISED.\n[Hint: Yes/y or No/n allowed only]")
            self.newTransact()
        
        
if __name__=='__main__':
    bankMe=BankAccount().transactionMsg()
   
