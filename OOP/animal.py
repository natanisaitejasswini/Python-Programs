class Animal(object):
  def __init__(self, name):
    print 'New Animal!!!'
    self.name = name
    self.health = 100
  def taunt(self):
    print "You want a piece of me?"

  def walk(self):
    self.health -= 1
    return self

  def run(self):
    self.health -= 5
    return self

  def displayHealth(self):
    print "Animal Name: " + (self.name)
    print "Animal Health: " + str(self.health)
    return self

Animal1 = Animal("Fish")
Animal1.walk().walk().walk().run().run().displayHealth()
print 50*'*'

class Dog(Animal):
  def __init__(self,name):
    super(Dog, self).__init__(name)
    self.health = 150

  def pet(self):
    self.health += 5
    return self


Dog1 = Dog("duck")
Dog1.walk().walk().walk().run().run().pet().displayHealth()
print 50*'*'

class Dragon(Animal):
  def __init__(self,name):
    super(Dragon, self).__init__(name)
    self.health = 170

  def displayHealth(self):
    print "This is Dragon"
    super(Dragon, self).displayHealth()

  def fly(self):
    self.health -= 10
    return self
Dragon1 = Dragon("Giant Dragon ")
Dragon1.walk().walk().walk().run().run().fly().fly().displayHealth()

