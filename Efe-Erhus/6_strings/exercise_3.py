#place your code here
#3
def char_count(q_string,q_char):
	count=0
	for char in q_string:
		if char==q_char:
			count+=1
	return count