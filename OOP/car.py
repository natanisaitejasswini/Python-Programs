class Car(object):
  def __init__(self, price, speed, fuel, mileage):
    print "New Car!"
    self.price = price 
    self.speed = speed 
    self.fuel = fuel
    self.mileage = mileage
    if self.price >= 10000:
      self.tax = 0.15
    else:
      self.tax = 0.12
    self.display_all()
  def display_all(self):
    print "Price:" + str(self.price)
    print "Speed:" + str(self.speed)
    print "Fuel:" + str(self.fuel)
    print "Mileage:" + str(self.mileage)
    print "Tax:" + str(self.tax)

car1 = Car(2000, "35mph", "Full", "15mpg")
print 25*'*'
car2 = Car(2000, "5mph", " Not Full", "105mpg")
print 25*'*'
car3 = Car(2000, "15mph", "Kind of Full", "95mpg")
print 25*'*'
car4 = Car(2000, "25mph", "Full", "25mpg")
print 25*'*'
car5 = Car(2000, "45mph", "Empty", "25mpg")
print 25*'*'
car6 = Car(20000000, "35mph", "Empty", "15mpg")







