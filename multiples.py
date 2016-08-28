
#1 (1 to 1000 odd numbers)
for count in range(1,1000):
	if count % 2 == 1:
		print  "number", count, "odd"
	count += 1


#2 multiples of 5
for count in range(5,1000000):
	if count % 5 == 0:
		print "number ", count, "is multiple of 5"
	count += 1
