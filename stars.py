def drawstars(A):
	for i in A:
		B = '*'
		if isinstance(i,int):
			print B * int(i)
		else:
			print i[0].swapcase() * len(i)
print drawstars([4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"])
