from datetime import datetime
from datetime import timedelta
from functions import in_progress
class Account:
    def __init__(self,acc_name,acc_num,passk):
        self.name=acc_name
        self.number=acc_num
        self.bal=0
        self.passk=passk
        self.barred=0
    def bar_account(self,mins=5):
        self.barred=datetime.now()+timedelta(minutes=mins)
    def is_barred(self):
        if self.barred==0:
            return False
        else:
            if datetime.now()>self.barred:
                self.barred=0
                return False
            else:
                return True
    def time_left_barred(self):
        span=self.barred-datetime.now()
        minutes=span.seconds//60
        seconds=span.seconds%60
        return [minutes,seconds] 
    def verify_Security_key(self):
        for r in range(3):
            passk=input("Please Enter your Security Key:\t")
            r+=1
            if passk==self.passk:
                return True
            elif r==3:
                print("You have Exhausted the allowed Number of Trials")
                print("Your Account has been barred for 5mins")
                self.bar_account()
                return False
            else:
                print("Your Security Key is incorrect.\nYou have {} more trials".format(3-r))
                continue
    def change_security_key(self):
        if not self.verify_Security_key():
            print("Operation failed")
            return
        while True:
            newpsk=input("Please Enter New Security Key:\t")
            newpsk2=input("Please re-enter New Security Key:\t")
            if newpsk==newpsk2:
                self.passk=newpsk
                in_progress()
                print("Security Key Changed")
                return
            else:
                print("Keys do not match")
    