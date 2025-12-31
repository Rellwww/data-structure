#DoublyLinkedlist
class DoublyNode:
  def __init__(self,val):
    self.val=val
    self.next=None
    self.prev=None

class DoublyLinkedList:
  #Dummy Node
  def __init__(self):
    self.head=DoublyNode(None)
    self.tail=DoublyNode(None)
    self.head.next=self.tail
    self.tail.prev=self.head
    self.size=0
#tool APIs
  def __str__(self):
    values=[]
    cur=self.head.next
    while cur.next:
      values.append(str(cur.val))
      cur=cur.next
    return "->".join(values)+"->None"
  
  def size(self):
    return self.size
  
  def is_empty(self):
    return self.size==0
  
  def is_element_index(self,index):
    return 0 <= index < self.size
  
  def is_position_index(self,index):
    return 0 <= index <= self.size
  
  def check_element_index(self,index):
    if not self.is_element_index(index):
      raise IndexError(f"Index:{index}, Size:{self.size}")
    
  def check_position_index(self,index):
    if not self.is_position_index(index):
      raise IndexError(f"Index")
    
  def get_node(self,index):
    self.check_element_index(index)
    p=self.head.next
    for _ in range(index):
      p=p.next
    return p

  def display(self):
    print(f"Size={self.size}")
    p=self.head.next





#add element
  def add_last(self,val):
    x=DoublyNode(val)
    x.prev=self.tail.prev
    x.next=self.tail
    self.tail.prev.next=x
    self.tail.prev=x
    self.size+=1

  def add_first(self,val):
    p=DoublyNode(val)
    p.prev=self.head
    p.next=self.head.next
    self.head.next.prev=p
    self.head.next=p
    self.size+=1
    
#  def add_index(self,val,index):

  

if __name__=="__main__":
  list = DoublyLinkedList()
  list.add_last(1)
  list.add_first(0)
  list.add_first(-1)
  list.add_last(2)
  print(list.is_empty())
  print(list)

  
    
    
