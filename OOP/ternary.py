def square(num):
  x = num ** 2
  return x
print square(4)
print 50*'*'

sqrt = lambda num: num ** 2 
print sqrt(4)
print 50*'*'

adder= lambda x: x + 2
print adder(9)
print 50*'*'

# An element in list
my_list = ['test_string', 99, lambda x : x ** 2]
print my_list[1]
print 25*'*'
print my_list[2](5)  # 5 is X here
print 50*'*'

# create a list
my_arr = [1,2,3,4,5]
def square(num):
  return num ** 2
print map(square, my_arr)
print 50*'*'

# Function once
my_arr = [1,2,3,4,5]
print map(lambda x: x ** 2, my_arr)
print 50*'*'

#CALL BACK
def invoker(callback):
    # invoke the input pass the argument 2
    print callback(2)
invoker(lambda x: 2 * x)
invoker(lambda y: 5 + y)
print 50*'*'

#Stored in a variable
add10 = lambda x: x + 10 # store lambda expression in a variable
print add10(2)  # returns 12
print add10(98) 
print 50*'*'

#
animals = ['monkey','cat','dog','eagle','emu','seal']
print sorted(animals,key = len)
print 50*'*'
print sorted(animals, key = lambda x: x.find('e'))


