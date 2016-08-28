# def varargs(arg1, *restOfArg):
#  print "restOfArg is of " + str(type(restOfArg))
#  varargs("one", "two", "three")
#  # restOfArg is of <type 'tuple'>
# print varargs()

# Addition
class MathDojo(object):
  def __init__(self):
    print "MathDojo"
    self.result = 0
    # num is tuple
  def add(self, *num): 
    for item in num:
      self.result += item
    print "Added"
    return self

  def sub(self, *num):
    for item in num:
      self.result -= item
    print "Substracted"
    return self
# md is instance --- we are creating
md = MathDojo()
print md.add(2).add(2,5).sub(3,2).result

    
