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
