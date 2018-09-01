def grader(a):
    if a < 40:
        print("F3")
    elif a <=40 and a < 45:
        print('F2')
    elif a <=45 and a < 50 :
        print("F1 Supp")
    elif a<=50 and a < 60 :
        print("Third")
    elif a<=60 and a <70:
        print("Second")
    elif a<=70 and a<75:
        print('Upper second')
    elif a>=75:
        print("First")
xs = [ 83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,
49.9, 45, 44.9, 40, 39.9, 2, 0]

for grade in xs:
    print(grader(grade))
