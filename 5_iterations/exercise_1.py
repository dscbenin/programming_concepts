def countodd(x):
    oddNumbers = 0
    for i in x:
        if i%2 == 1:
            oddNumbers += 1
    return oddNumbers

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Total odd numbers =", str(countodd(x)))