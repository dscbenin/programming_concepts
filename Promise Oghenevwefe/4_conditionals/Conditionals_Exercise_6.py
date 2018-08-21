# Write a function which is given an exam mark and it returns a string
# the grade for that mark

def exam_grade(examMark):
    if examMark >= 75 and examMark <= 100:
        return 'First'
    elif examMark >= 70 and examMark < 75:
        return 'Upper Second'
    elif examMark >= 60 and examMark < 70:
        return 'Second'
    elif examMark >= 50 and examMark < 60:
        return 'Third'
    elif examMark >= 45 and examMark < 50:
        return 'F1 Supp'
    elif examMark >= 40 and examMark < 45:
        return 'F2'
    elif examMark >= 0 and examMark < 40:
        return 'F3'
    else:
        return 'Invalid Mark'

examMark = int(input("Enter the Exam mark: "))
print("Your grade is:  "+ exam_grade(examMark))
