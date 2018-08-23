import random
import operator
deck = []
for v in range(1,14):
	deck.append((v,'C'))
	deck.append((v,'S'))
	deck.append((v,'H'))
	deck.append((v,'D'))
random.shuffle(deck)
draw = deck[1:14]

def getkey(item):
	return item[1]

draw.sort()
draw.sort(key=operator.itemgetter(1))
print(draw)

'''
gbern$ python deck.py 
[(6, 'C'), (8, 'C'), (9, 'C'), (1, 'D'), (6, 'D'), (8, 'D'), (9, 'D'), (1, 'H'), (6, 'H'), (11, 'H'), (3, 'S'), (7, 'S'), (13, 'S')]
'''
