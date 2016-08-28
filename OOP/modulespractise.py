import arithmetic
print arithmetic.add(5, 8)
print arithmetic.subtract(10, 5)
print arithmetic.multiply(12, 6)
print 50*'*'


import random # import the random module
class Human(object): #Define a new Human Class
  def __init__(self, clan=None): #Define a parameter with a default value, clan
    print 'New Human!!!'
    # Define attributes
    self.health = 100
    self.clan = clan
    self.strength = 3
    self.intelligence = 3
    self.stealth = 3
    # Define Methods
  def taunt(self):  #PASS self into all methods to access attributes
    print "You want a piece of me?"
  # inserted a new function so our Human instances can attack
  def attack(self):
    self.taunt()
    # use the random module to generate a number when we attack
    luck = round(random.random() * 100)
    if(luck > 50):
      if(luck * self.stealth > 150):
        print 'attacking!'
        return True
      else:
        print 'attack failed'
        return False
    else:
      self.health -= self.strength 
      print "attack failed"
      return False
mike = Human()
mike.taunt()
mike.attack()
print mike
