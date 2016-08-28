

def score(A):
	print 'Scores and Grades'
	for i in A:
		if i >= 90 and i <= 100:
			print 'Score:', i ,'; Your grade is A'
		elif i >= 80 and i <= 89:
			print 'Score:', i, '; Your grade is B'
		elif i >= 70 and i <= 79:
			print 'Score:', i, '; Your grade is C'
		elif i >= 60 and i <= 69:
			print 'Score:', i, '; Your grade is D'
	print 'End of the Program. Bye!'
print score([87,67,95,100,75, 90, 89, 72,60, 98])