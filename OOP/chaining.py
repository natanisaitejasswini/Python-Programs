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
    return self

  def ride(self):
    print "Riding"
    self.miles += 10
    return self

  def reverse(self):
    print "Reversing"
    if self.miles >= 5:
      self.miles -= 5
    return self

bike1 = Bike(200, "25mph")
bike1.ride().ride().ride().reverse().displayInfo()
print 25*'*'

bike2 = Bike(400, "55mph")
bike2.ride().ride().reverse().reverse().displayInfo()
print 25*'*'

bike3 = Bike(800, "90mph")
bike3.reverse().reverse().reverse().displayInfo()
print 25*'*'














