def replace(s, old, new):
    temp=s.split(old)
    print(temp)
    return new.join(temp)

s="I feel xxxx for the last time"
old, new="xxxx", "fear"
print(replace(s, old, new))
