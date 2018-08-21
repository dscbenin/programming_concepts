def grade_this_score(scoreList):
        if (score >= 75):
            return str(score) + " : First"
        elif(score >= 70 and score< 75):
            return str(score) + " : Upper Second" 
        elif(score >= 60 and score < 70):
            return str(score) + " : Second"
        elif(score >= 50 and score < 60):
            return str(score) + " : Third"
        elif(score >= 45 and score < 50):
            return str(score) + " : F1 Supp"
        elif(score >= 40 and score < 45):
            return str(score) + " : F2"
        else:
            return str(score) + " : F3"
        
xs= [83.9999, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]
print("Score : Grade")
for score in xs:
    print(grade_this_score(xs))
