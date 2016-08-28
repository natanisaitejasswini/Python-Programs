import random
import string
def randomString(val):
	letters = string.letters
	return "".join(random.choice(letters) for i in range(val))
def makeRandom():
	return [random.randint(5,45) if random.randint(0,1) else randomString(random.randint(2,7)) for y in range(10)]
print makeRandom()


def suprise():
	# list = makeRandom()
	for i in makeRandom():
		B = '@'
		if isinstance(i,int):
			print B * int(i)
		elif i[0].istitle():
			print(i[0],len(i))
		else:
			print i [::-1]
print suprise()