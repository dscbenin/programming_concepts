#paste your bank app in this folder
#Efe's Bank
class Bank:
    def __init__(self,name):
        self.name=name
        self.accs=[]
        #pointer for account number
        self.num=117
    def create_account(self):
        acc_name=input("Enter your Preferred Account Name:\t")  
        acc=Account(acc_name,self.num)
        self.accs.append(acc)
        #increase account number for next assignment
        self.num+=1
        print("#"*30)
        print("Account Created")
        print("#"*30)
        print("Account Name:\t\t",acc.name)
        print("Account Number:\t\t",acc.number)
        print("Account Balance:\t",acc.bal)
    def check_balance(self):
        temp=input("Please Enter Your Acount Name or Account number:\t")
        for acc in self.accs:
            if (acc.name==temp or acc.number==int(temp)):
                print()
                print()
                print()
                print("#"*30)
                print("Account balance")
                print("#"*30)
                print("Account Name:\t\t",acc.name)
                print("Account Number:\t\t",acc.number)
                print("Account Balance:\t",acc.bal)
                return
        print("Account not Found")
    def deposit(self):
        temp=input("Please Enter Your Acount Name or Account number:\t")
        amount=float(input("Please Enter the Amount you Want to Deposit:\t"))
        for acc in self.accs:
            if (acc.name==temp or acc.number==int(temp)):
                print()
                print()
                print()
                print("#"*30)
                print("Deposit Slip")
                print("#"*30)
                print("Account Number:\t\t",acc.number)
                print("Previous Balance:\t",acc.bal)
                acc.bal+=amount
                print("Current Balance:\t",acc.bal)
                return
        print("Account Not Found")
    def withdraw(self):
        temp=input("Please Enter Your Acount Name or Account number:\t")
        amount=float(input("Please Enter the Amount you Want to Withdraw:\t"))
        for acc in self.accs:
            if (acc.name==temp or acc.number==int(temp)):
                print()
                print()
                print()
                print("#"*30)
                print("Withdrawal Slip")
                print("#"*30)
                print("Account Number:\t\t",acc.number)
                print("Previous Balance:\t",acc.bal)
                if acc.bal<amount:
                    print("Insufficient Funds")
                    return
                acc.bal-=amount
                print("Current Balance:\t",acc.bal)
                return
        print("Account Not Found")

class Account:
    def __init__(self,acc_name,acc_num):
        self.name=acc_name
        self.number=acc_num
        self.bal=0
bank=Bank("Efe's Bank")
while True:
    print("#"*30)
    print("Welcome To Efe's Bank")
    print("#"*30)
    print("What would you Like to do?")
    ops=["open an account", "Make Withdrawals", "Deposit Cash", "Check Balance"]
    i=1
    for op in ops:
        print(i,"\t\t",op)
        i+=1
    while True:
        try:
            resp=int(input("Please Make Your Selection\t\t"))
            if resp not in [1,2,3,4]:
                raise Exception("Invalid Selection")
        except:
            print("Invalid input")
            continue
        else:
            break
    if resp==1:
        bank.create_account()
    elif resp==2:
        bank.withdraw()
    elif resp==3:
        bank.deposit()
    elif resp==4:
        bank.check_balance()
    else:
        print("Please make a valid selection")
        resp=int(input())
    temp=input("Do you want to perform another operation?Y/N\t")
    if temp.lower()=="y":
        continue
    else:
        print("Thank you for Using our Services")
        break
print("GoodBye!!!")
print()
exit()
