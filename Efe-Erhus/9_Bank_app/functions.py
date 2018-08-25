
import os
from datetime import datetime
from datetime import timedelta
from time import sleep
def print_date():
    dt=datetime.now()
    print(dt.strftime("%B %d, %Y  %H:%M:%S"))
def in_progress():
    print("loading...")
    for i in range(3):
        sleep(0.3)
        print("...",)   
    print()
def clear_screen():
    os.system("cls")

