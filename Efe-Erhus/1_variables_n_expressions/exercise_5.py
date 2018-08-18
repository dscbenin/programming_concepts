#place your code here
#5
#i think that formular should be r/100 not r/n
p=10000
n=12
r=8
t=float(input("Please Enter the number of years the money will be compounded for\t"))
a=p*(1+r/n)**(n*t)
print("The final amount after t years is:\t",a)