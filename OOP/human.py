class Human(object):
    pass
michael = Human()
jimmy = Human()
print michael
print 50*'*'

# taunt
class Human(object):
  def taunt(self):     # note how we have a single parameter, 'self'
    print "You want a piece of me?"
michael = Human()
michael.taunt()     
print 50*'*'

# PRINT whenever we create new human
class Human(object):
    def __init__(self):
      print "New Human!!!"     #when we create a new human, we'll get this as an output
    def taunt(self):
      print "You want a piece of me?"
Tom = Human()
Tom.taunt()
print Tom
print 50*'*'

# Counting distance
class Point(object):
    def __init__(self,x = 0,y = 0):
        print "Created a new point!"
        self.x = x
        self.y = y
    def distance(self):
        #Find distance from origin
        return (self.x**2 + self.y**2) ** 0.5
mike = Point()
print mike
print 50*'*'