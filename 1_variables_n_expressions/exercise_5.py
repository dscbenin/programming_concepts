P=10000
r=0.08
n=12
t=int(input("Enter the number of years for the investment: "))
A= P*(1 + r/n)**(n*t)
print("${:,.2f} after {} years.".format(A, t))
