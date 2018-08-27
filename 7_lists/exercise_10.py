

def replace(s, old, new):
    d = s.split(old)
    print(s)
    newWord = new

    return newWord.join(d)

s = "Hi I'm Deadpool"
print(replace(s, "oo", "il"))
