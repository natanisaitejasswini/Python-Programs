class MathDojo(object):
	def __init__(self):
		print "MathDojo"
		self.result = 0
	def add(self, *items): 
		for item in items:
			try:
				for i in item:
					self.result = self.result + i
			except TypeError:
				self.result += item
		# for item in items:
		# 	if type(item) in (int,float):
		# 		self.result = self.result + item
		# 	elif type(item) in (list,tuple):
		# 		for x in item:
		# 			self.result = self.result + x
		return self
	def substract(self, *items):
		for item in items:
			if type(item) in (list,tuple):
				for x in item:
					self.result = self.result - x
			elif type(item) in (int,float):
				self.result = self.result - item
		return self
md1 = MathDojo()
print md1.add(2).add(2, 5).substract(3, 2).result
print 25*'*'
md2 = MathDojo()
tup = (1,2,3)
print md2.add(tup,[1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).substract(2, [2,3], [1.1, 2.3]).result
print 25*'*'
md3 = MathDojo()
print md3.add(0.5,1.0).result
 		
