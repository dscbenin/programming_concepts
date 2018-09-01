def replace(s,old,new):
    list1 = s.split(old)
    c = new.join(list1)
    print(c)


print(replace('Jack is a bad boa',"a","o"))
