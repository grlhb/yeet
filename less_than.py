less = []
def less_than(original,n):
	for i in original:
		if i < n:
			less.append(i)
	return less 


'''
original = [1,2,4,7,9]
less_than(original,6)
print(less)
gbern$ python less_than.py 
[1, 2, 4]
'''

