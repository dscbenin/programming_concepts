# Write a function replace(s, old, new), that replaces all occurences of old with new

def replace(s, old, new):
    newList = s.split(old)
    print(s)
    glue = new
    
    return glue.join(newList)
    

s = "I love spom! Spom is my favorite food, Spom, spom, yum!"

print(replace(s, "o", "a"))
