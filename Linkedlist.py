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
    if index < (self.size // 2):
      p=self.head.next
      for _ in range(index):
        p=p.next
    else:
      p=self.tail.prev
      back_step_num=self.size-index-1
      for _ in range(back_step_num):
        p=p.prev
    return p

  def display(self):
    print(f"Size={self.size}")
    p=self.head.next
    while p!=self.tail:
      print(f"{p.val} <-> ",end="")
      p=p.next
    print("None\n")

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
    
  def add_index(self,index,element):
    self.check_position_index(index)
    if index==self.size:
      self.add_last(element)
      return
    p=self.get_node(index)
    x=DoublyNode(element)
    x.prev=p.prev
    x.next=p
    p.prev.next=x
    p.prev=x
    self.size+=1

#delete element
  def remove_first(self):
    if self.size<1:
      raise IndexError("No elements to remove")
    x=self.head.next
    self.head.next=x.next
    x.next.prev=self.head
    x.prev=None
    x.next=None
    self.size-=1
    return x.val
  
  def remove_last(self):
    if self.size<1:
      raise IndexError("No elements to remove")
    x=self.tail.prev
    x.prev.next=self.tail
    self.tail.prev=x.prev
    x.prev=None
    x.next=None
    self.size-=1
    return x.val
  
  def remove(self,index):
    self.check_element_index(index)
    x=self.get_node(index)
    p=x.next
    p.prev=x.prev
    x.prev.next=p
    x.next=None
    x.prev=None
    self.size-=1
    return x.val
  
#find element
  def get(self,index):
    self.check_element_index(index)
    p=self.get_node(index)
    return p.val
  
  def get_first(self):
    if self.size<1:
      raise IndexError("No element in the list")
    return self.head.next.val
  
  def get_last(self):
    if self.size<1:
      raise IndexError("No element in the list")
    return self.tail.prev.val
  
  #change element
  def set(self,index,val):
    self.check_element_index(index)
    p=self.get_node(index)
    old_val=p.val
    p.val=val
    return old_val


#SinglylinkedList
class SinglyLinkedList:
  class Node:
    def __init__(self,val):
      self.val=val
      self.next=None
  
  def __init__(self):
    self.head=self.Node(None)
    self.tail=self.head
    self.size=0
#tool APIs
  def get_size(self):
    return self.size
  
  def is_empty(self):
    return self.size==0
  
  def is_element_index(self,index):
    return 0<=index<self.size
  
  def is_position_index(self,index):
    return 0<=index<=self.size
  
  def check_element_index(self,index):
    if not self.is_element_index(index):
      raise IndexError(f"Index:{index},Size:{self.size}")
    
  def check_position_index(self,index):
    if not self.is_position_index(index):
      raise IndexError(f"Index:{index},Size:{self.size}")

# add element    
  def add_first(self,elememt):
    new_node=self.Node(elememt)
    new_node.next=self.head.next
    self.head.next=new_node
    if self.size==0:
      self.tail=new_node
    self.size+=1

  def add_last(self,element):
    new_node=self.Node(element)
    self.tail.next=new_node
    self.tail=new_node
    self.size+=1

  def add_index(self,index,element):
    self.check_position_index(index)
    if index==self.size:
      self.add_last(element)
      return 
    p=self.head
    for _ in range(index):
      p=p.next
    new_node=self.Node(element)
    new_node.next=p.next
    p.next=new_node
    self.size+=1

  def remove_first(self):
    if self.is_empty():
      raise Exception("No element in list")
    p=self.head.next
    self.head.next=p.next
    if self.size==1:
      self.tail=self.head
    self.size-=1
    return p.val
  
  def remove_last(self):
    if self.is_empty():
      raise Exception("No element in list") 
    p=self.head
    while p.next !=self.tail:
      p=p.next
    val=self.tail.val
    self.tail=p
    p.next=None
    self.size-=1
    return val
  
  def remove(self,index):
    self.check_element_index(index)
    p=self.head
    for _ in range(index):
      p=p.next
    temp=p.next
    p.next=temp.next
    if index==self.size-1
      self.tail=p
    self.size-=1
    return temp.val
#find element  
  def get_first(self):
    if self.is_empty():
      raise Exception("No element exception")
    return self.head.next.val
  
  def get_last(self):
    if self.is_empty():
      raise Exception("No element excetion")
    return self.tail.val
  
  def get(self,index):
    self.check_element_index(index)
    p=self.head
    for _ in range(index):
      p=p.next
    return p.val
  
#change element  
  def set(self,index,element):
    self.check_element_index(index)
    p=self.head
    for _ in range(index):
      p=p.next
    old_val=p.val
    p.val=element
    return old_val





  

  

if __name__=="__main__":
  list = DoublyLinkedList()
  list.add_last(1)
  list.add_first(0)
  list.add_first(-1)
  list.add_last(2)
  print(list.is_empty())
  list.display()
  list.add_index(4,3)
  list.display()
  print(list.remove_first())
  print(list.remove_last())
  list.display()
  list.add_last(3)
  list.remove(3)
  print(list.get_first())
  print(list.get_last())
  list.set(2,11)
  list.display()

  
    
    
