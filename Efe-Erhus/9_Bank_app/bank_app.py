#paste your bank app in this folder
from account import Account
from functions import *
#Efe's Bank
class Bank:
    def __init__(self,name):
        self.name=name
        self.accs=[]
        #pointer for account number
        self.num=117
        self.open()
    def open(self):
        while True:
            print("#"*30)
            print("Welcome To {}".format(self.name))
            print("#"*30)
            print("What would you Like to do?")
            ops=["open an account", "Make Withdrawals", "Deposit Cash", "Check Balance","Transfer","Change Security Key"]
            i=1
            for op in ops:
                print(i,"\t\t",op)
                i+=1
            while True:
                try:
                    resp=int(input("Please Make Your Selection\t\t"))
                    if resp not in [1,2,3,4,5,6]:
                        raise Exception("Invalid Selection")
                except:
                    print("Invalid input")
                    continue
                else:
                    break
            if resp==1:
                in_progress()
                self.create_account()
            elif resp==2:
                in_progress()
                self.withdraw()
            elif resp==3:
                in_progress()
                self.deposit()
            elif resp==4:
                in_progress()
                self.check_balance()
            elif resp==5:
                in_progress()
                self.transfer()
            elif resp==6:
                in_progress()
                self.change_security_key()
            temp=input("Do you want to perform another operation?Y/N\t")
            if temp.lower()=="y":
                clear_screen()
                continue
            else:
                self.close()
                break   
    def create_account(self):
        while True:
            try:
                acc_name=input("Enter your Preferred Account Name:\t")
                if acc_name=="":
                    raise Exception("Empty input.\nPlease try again")
                if len(acc_name)<3:
                    raise Exception("Please Enter at least 3 characters")
            except Exception as err:
                print(err)
            else:
                break
        while True:
            try:
                acc_pass=input("Enter your Preferred Security Key Name:\t")
                if acc_pass=="":
                    raise Exception("Empty input.\nPlease try again")
                if len(acc_pass)<3:
                    raise Exception("Please Enter at least 3 characters")
            except Exception as err:
                print(err)
            else:
                break
        acc=Account(acc_name,self.num,acc_pass)
        self.accs.append(acc)
        #increase account number for next assignment
        self.num+=1
        in_progress()
        print("#"*30)
        print("Account Created")
        print("#"*30)
        print_date()
        print("Account Name:\t\t",acc.name)
        print("Account Number:\t\t",acc.number)
        print("Account Balance:\t$",acc.bal)
    def check_balance(self):
        temp=input("Please Enter Your Acount Name or Account number:\t")
        acc=self.find_account(temp)
        in_progress()
        if acc is not None:
            #barred check
            if acc.is_barred():
                tl=acc.time_left_barred()
                print("This account is barred.\nPlease try again in {}minutes and {}seconds".format(tl[0],tl[1]))
                return
            if not acc.verify_Security_key():
                return
            print("#"*30)
            print("Account balance")
            print("#"*30)
            print("Account Name:\t\t",acc.name)
            print("Account Number:\t\t",acc.number)
            print("Account Balance:\t$",acc.bal)
            return
        print("Account not Found")
    def deposit(self):
        #find account name
        temp=input("Please Enter Your Acount Name or Account number:\t")
        while True:
            try:
                amount=float(input("Please Enter the Amount you Want to Deposit:\t$"))
            except:
                print("Please enter a Valid Amount")
            else: 
                break
        acc=self.find_account(temp)
        in_progress()
        if acc is not None:
            print("#"*30)
            print("Deposit Slip")
            print("#"*30)
            print_date()
            print("Account Number:\t\t",acc.number)
            print("Previous Balance:\t$",acc.bal)
            acc.bal+=amount
            print("Current Balance:\t$",acc.bal)
            return
        print("Account Not Found")
    def withdraw(self):
        temp=input("Please Enter Your Acount Name or Account number:\t")
        while True:
            try:
                amount=float(input("Please Enter the Amount you Want to Withdraw:\t$"))
            except:
                print("Please enter a Valid Amount")
            else: 
                break
        acc=self.find_account(temp)
        in_progress()
        if acc is not None:
            #barred check
            if acc.is_barred():
                tl=acc.time_left_barred()
                print("This account is barred.\nPlease try again in {}minutes and {}seconds".format(tl[0],tl[1]))
                return
            #Verify Security Key
            if not acc.verify_Security_key():
                print("Transaction Failed")
                return
            print()
            print()
            print()
            print("#"*30)
            print("Withdrawal Slip")
            print("#"*30)
            print_date()
            print("Account Number:\t\t",acc.number)
            print("Previous Balance:\t$",acc.bal)
            if acc.bal<amount:
                print("Insufficient Funds")
                return
            acc.bal-=amount
            print("Current Balance:\t ${}".format(acc.bal))
            return
        print("Account Not Found")
    def transfer(self):
        sender=input("Please Enter Your Acount Name or Account number:\t")
        while True:
            try:
                amount=float(input("Please Enter the Amount you Want to Transfer:\t$"))
            except:
                print("Please enter a Valid Amount")
            else: 
                break
        sender=self.find_account(sender)
        if sender is not None:
            #barred check
            if sender.is_barred():
                tl=sender.time_left_barred()
                print("This account is barred.\nPlease try again in {} minutes and {} seconds".format(tl[0],tl[1]))
                return
            if not sender.verify_Security_key():
                return
            reciever=input("Please Enter the Reciever's Acount Name or Account number:\t")
            reciever=self.find_account(reciever)
            if reciever is not None:
                confirm=input("You are transferring ${} from {} to {}.\nEnter Y to confirm or N to cancel:\t".format(amount,sender.name,reciever.name))
                if confirm.lower()!="y":
                    return
                in_progress()
                if sender.bal<amount:
                    print("Insufficient funds")
                    return
                else:
                    print("Transaction Successful")
                    print("#"*30)
                    print("Transaction Slip")
                    print("#"*30)
                    print_date()
                    print("Account Number:\t\t{}".format(sender.number))
                    print("Previous Balance:\t${}".format(sender.bal))
                    sender.bal-=amount
                    reciever.bal+=amount
                    print("Current Balance:\t ${}".format(sender.bal))
                    return
            else:
                print("Reciever not found")
                return
        else:
            print("Account not found")
        return
    def change_security_key(self):
        temp=input("Please Enter Your Acount Name or Account number:\t")
        acc=self.find_account(temp)
        if acc is not None:
            #barred check
            if acc.is_barred():
                tl=acc.time_left_barred()
                print("This account is barred.\nPlease try again in {}minutes and {}seconds".format(tl[0],tl[1]))
                return
            acc.change_security_key()
        else:
            print("Account not found")
    def find_account(self,input):
        try:
            input=int(input)
            for acc in self.accs:
                if input==acc.number:
                    return acc
                else:
                    return None
        except:
            for acc in self.accs:
                if input==acc.name:
                    return acc
    def close(self):
        print()
        print("Thank you for Using our Services")
        print("GoodBye!!!")
        input("Push any key to exit")
        exit()

bank=Bank("Efe's Bank")
