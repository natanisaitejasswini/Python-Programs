"""
map => Take a list and a function, and return the list you get by applying that function to every item in the list 

	filter => Take a list and return only the values when a given function is true 

my_filter([1,2,3,4,5], lambda x: x%2==0) => [2,4]

	reject => The exact opposite of filter

my_reject([1,2,3,4,5], lambda x: x%2==0) => [1,3,5]

	find  => Return the first value in the list where the function is true 

my_find([1,2,3,4,5], lambda x: x%2==0) => 2

	all => Return True if the function is true for every item in the list, false otherwise

my_all([1,2,3,4,5], lambda x: x%2==0) => False

	any => Return True if the function is true for any item in the list, false otherwise

my_any([1,2,3,4,5], lambda x: x%2==0) => True
"""

def my_map(lst, func):
	output = []
	for item in lst:
		# print("for loop")
		output.append(func(item))
		# print(item)
		# print(func(item))
	return output

def square(num):
	return num**2


a = [1,2,3,4,5]
print(my_map(a, square))

print(a)
Add Comment 