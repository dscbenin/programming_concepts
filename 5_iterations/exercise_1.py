def odd_no_counter(providedlist):
    odd_no=[]
    for i in providedlist:
        if(i%2==0):
            pass
        else:
            odd_no.append(i)
   # return odd_no
    return "Odd number(s) identified: {}, a total of {}".format(odd_no, str(len(odd_no)))        
xs=[4,3,4,5,6,0,9,2,1,1,11,3,5,6]
print(odd_no_counter(xs))
