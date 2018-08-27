#Computing the final amount if one is earning compound interest
#a=p(1+r/n)^n*t

p = 10000
n = 12
r = 0.08
t = int(input("Please input the number of years the money will be compounded for"))
a = p * (1 + r/n)**(n*t)
print(a)



