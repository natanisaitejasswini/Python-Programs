class Cat(object):
    pass
tejucat = Cat()
tejucat.color = 'orange'
tejucat.size = 'small'
tejucat.age = 5
print "tejucat color:", tejucat.color
print "tejucat size:", tejucat.size
print "tejucat age:", tejucat.age
print 50*'*'

# using __init__ to intialize attributes
class Cat(object):
  def __init__(self, color, type, age):
    self.color = color
    self.type = type
    self.age = age
saicat = Cat('orange', 'fat', 5)
print "saicat color:", saicat.color
print "saicat type:", saicat.type
print "saicat age:", saicat.age
print 25*'*'
tomcat = Cat('red', 'fat', 5)
print "tomcat color:", tomcat.color
print "tomcat type:", tomcat.type
print "tomcat age:", tomcat.age
print 50*'*'

# Applying same concept to Human
class Human(object):
    def __init__(self, clan=None):
      print "New Human!!!"     # when we create a new human, we'll get self as an output
                               # initialize the clan instance variable by passing in a value
      self.clan = clan
      # initialize more attributes that will be the same for all humans
      self.health = 100
      self.strength = 3
      self.intelligence = 3
      self.stealth = 3
    def taunt(self):
      print "You want a piece of me?"
# create an instance of a human, pass in a class name
michael = Human('CodingDojo') # Here we are creating Human called michael 
print 'michaelhealth:', michael.health 
jimmy = Human('CodingNinjas')
michael.taunt()
print 50*'*'


# Default setting
class Test(object):
  def __init__(self, phrase='Nothing was passed'):     # set the default value for 'phrase' parameter
    print "This string was passed in: " + phrase
    self.phrase = phrase
test1 = Test('Hello, World!')
test2 = Test()
print "Test 1 has phrase: '" + test1.phrase + "'"
print "Test 2 has phrase, '" + test2.phrase + "'"
print 50*'*'
# distance calculation
class Point(object):
    def __init__(self,x = 0,y = 0):
        print "Created a new point!"
        self.x = x
        self.y = y
    def distance(self):
        #Find distance from origin
        return (self.x**2 + self.y**2) ** 0.5

        



