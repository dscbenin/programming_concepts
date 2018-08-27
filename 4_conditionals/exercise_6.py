def gradeSystem(grade):
    if grade >= 75:
        return "First"
    elif grade == [70-75]:
        return "Upper Second"
    elif grade == [60-70]:
        return "Second"
    elif grade == [50-60]:
        return "Third"
    elif grade == [45-50]:
        return "F1 Supp"
    elif grade == [40-45]:
        return "F2"
    elif grade < 40:
        return "F3"

grade = int(input("Please input your exam score"))
print ("Your grade is " + gradeSystem(grade) + ".")


