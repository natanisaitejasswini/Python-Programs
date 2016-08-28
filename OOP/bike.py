class Bike(object):
  def __init__(self, price, max_speed):
      print "New Bike!!"
      self.price = price
      self.max_speed= max_speed
      self.miles= 0

  def displayInfo(self):
    print "Price is: " + str(self.price)
    print "Max_speed is: " + str(self.max_speed)
    print "Miles are: " + str(self.miles)

  def ride(self):
    print "Riding"
    self.miles += 10

  def reverse(self):
    print "Reversing"
    if self.miles >= 5:
      self.miles -= 5

bike1 = Bike(200, "25mph")
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()
print 25*'*'

bike2 = Bike(400, "55mph")
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()
print 25*'*'

bike3 = Bike(800, "90mph")
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()
print 25*'*'







