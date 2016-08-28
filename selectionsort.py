def randomlist():
	list = []
	while (len(list) < 100):
		import random

		x = random.randint(0, 10000)
		list.append(x)

	return list

def selection_sorting(list):
	list = randomlist()
	for i in range(len(list)-1):
		min = i
		for j in range(i+1,len(list)):
			if list[j]<list[min]:
				list[j], list[min] = list[min], list[j]
				print list
	return list
print selection_sorting(list)