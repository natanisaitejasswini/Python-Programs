# 1...
def my_filter(my_list, func):
	output = []
	for item in my_list:
		if func(item):
			output.append(item)
	return output
print "my_filter function"
print my_filter([2,3,4,5], lambda x: x%2 == 0)
print 50*'*'

#2....
def my_reject(my_list, func):
	output = []
	for item in my_list:
		if not func(item):
			output.append(item)
	return output
print "my_reject function"
print my_reject([2,3,4,5], lambda x: x%2 == 0)
print 50*'*'

#3....
def my_find(my_list, func):
	for item in my_list:
		if func(item):
			return item
	return None
print "my_find function"
print my_find([2,3,3,5], lambda x: x%2 == 0)
print 50*'*'

#4....
def my_all(my_list, func):
	for item in my_list:
		if not func(item):
			return False
	return True
print "my_all function"
print my_all([2,1,3,7], lambda x: x%2 == 0)
print 50*'*'

#5....
def my_any(my_list, func):
	for item in my_list:
		if func(item):
			return True
	return False
print "my_any function"
print my_any([2,1,3,7], lambda x: x%2 == 0)
print 50*'*'

