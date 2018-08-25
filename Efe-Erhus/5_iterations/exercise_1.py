#place your code here
#1
def odd_num_in_list(x,mode=0):
	odd_num=[]
	for elem in x:
		if elem%2==1:
			odd_num.append(elem)
	if mode==0:
		return len(odd_num)
	elif mode==1:
		return odd_num