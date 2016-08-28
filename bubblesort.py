def randomlist():
	list = []
	while (len(list) < 100):
		import random

		x = random.randint(0, 10000)
		list.append(x)

	return list

def bubble_sorting(list):
	list = randomlist()
	for i in range(len(list)-1):
		for j in range(len(list) - 1 - i):
			if list[j] > list[j+1]:
				list[j], list[j + 1] = list[j + 1], list[j]
	return list
print bubble_sorting(list)


# Bubblesort
