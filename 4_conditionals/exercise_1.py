def days_of_the_week(x):
    if x == 0:
        return "Sunday"
    elif x == 1:
        return "Monday"
    elif x == 2:
        return "Tuesday"
    elif x == 3:
        return "Wednesday"
    elif x == 4:
        return "Thursday"
    elif x == 5:
        return "Friday"
    elif x == 6:
        return "Saturday"
    else:
        return "Please input a valid digit"

x = int(input("Please input your digit"))
print("The day of the week is " + days_of_the_week(x) +".")