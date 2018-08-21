# Assume the days of the week are numbered 0,1,2,3,4,5,6 from sunday to saturday
# Write a function which is given the day number, and it returns the day name(a string)

def day_of_the_week(dayNum):
    if dayNum == 0:
        return 'Sunday'
    elif dayNum == 1:
        return 'Monday'
    elif dayNum == 2:
        return 'Tuesday'
    elif dayNum == 3:
        return 'Wednesday'
    elif dayNum == 4:
        return 'Thursday'
    elif dayNum == 5:
        return 'Friday'
    elif dayNum == 6:
        return 'Saturday'
    else:
        return 'Invalid Choice'

dayNum = int(input("Enter the day of the week between 0 and 6, for Sunday to Saturday: "))
print("The day of the week is "+day_of_the_week(dayNum))
