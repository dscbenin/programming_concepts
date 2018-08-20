import datetime as dt
import os
import time

now = dt.datetime.now()
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
