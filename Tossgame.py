def toss():
	tries = 1
	head = 0
	tail = 0
	while tries <= 5000:
		import random
		x = random.random()
		coin = round(x)
		if coin == 1:
			head +=1
			print 'Attempt #', tries, ': Throwing a coin....Its a head!......Got', head, 'head(s) so far and', tail, 'tail(s) so far'
			tries +=1
		else:
			tail +=1
			print 'Attempt #', tries, ': Throwing a coin....Its a tail!......Got', head, 'head(s) so far and', tail, 'tail(s) so far'
			tries += 1
print toss()

