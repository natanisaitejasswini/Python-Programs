class SLNode(object):
  def __init__(self, val):
      self.value = val
      self.next = None
  def __str__(self):
    return "Node with value {}".format(self.value)

class SLList(object):
  def __init__(self):
    self.head = None
  def add_to_front(self,val):
    temp = self.head
    self.head = SLNode(val)
    self.head.next = temp
    return self
  def __str__(self):
    output = ""
    runner = self.head
    while runner:
      output += "[{}] ==> ".format(runner.value)
      runner = runner.next
    return output
my_node = SLNode(5)
print my_node
print 50*'*'

my_list = SLList()
my_list.add_to_front(4).add_to_front("Q")
print my_list
print 50*'*'









