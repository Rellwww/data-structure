#define singly linked list
class ListNode:
  def __init__(self,x):
    self.val=x
    self.next=None

  def createLinkedList(arr:list) -> 'ListNode':
    if arr is None or len(arr)==0:
      return None
    
    head=ListNode(arr[0])
    cur=head
    for i in range (1,len(arr)):
      cur.next=ListNode(arr[i])
      cur=cur.next
    return head
  
  def __str__(self):
    values=[]
    cur=self
    while cur:
      values.append(str(cur.val))
      cur=cur.next

    return "->".join(values)+"->None"

#class LinkedList:
#  def __init__(self):
#    self.head=None
  
#  def add_at_head(self,val):
#    new_node=ListNode(val)
#    new_node.next=self.head
#    self.head=new_node

class DoublyListNode:
  def __init__(self,x):
    self.val=x
    self.next=None
    self.prev=None
  
  def createDoublyLinkedList(arr:list)->'DoublyListNode':
    if not arr:
      return None
    head=DoublyListNode(arr[0])
    cur=head
    for val in arr[1:]:
       p=DoublyListNode(val)
       p.prev=cur
       cur.next=p
       cur=cur.next
    
    return head
  
  def __str__(self):
    values=[]
    cur=self
    while cur:
      values.append(str(cur.val))
      cur=cur.next
    return "->".join(values)+"->None"

if __name__=="__main__":
  head=DoublyListNode.createDoublyLinkedList([0,1,2,3,4,5,6])
  p=head
  while p:
    print(p.val)
    tail=p
    p=p.next
  p=tail
  while p.prev:
    print(p.val)
    p=p.prev
  print(p.val)
  new_head=DoublyListNode(-1)
  new_head.next=head
  head.prev=new_head
  head=new_head
  print(head)
  tail=head
  while tail.next:
    tail=tail.next
  new_node=DoublyListNode(7)
  tail.next=new_node
  new_node.prev=tail
  print(head)


"""  
if __name__=="__main__":  
  head=ListNode.createLinkedList([1,2,3,4,5,6])
  print(head)
  newnode=ListNode(0)
  newnode.next=head
  #head=newnode
  print(newnode)
  newnode=ListNode(7)
  p=head
  while p.next:
    p=p.next   
  p.next=newnode
  print(head)
  p=head
  for _ in range(2):
    p=p.next
  newnode=ListNode(33)
  newnode.next=p.next
  p.next=newnode
  print(head)
  p=head
  for _ in range(2):
    p=p.next
  p.next=p.next.next
  print(head)
  p=head
  while p.next.next:
    p=p.next
  p.next=None
  print(head)
  p=head
  head=p.next
  print(head)
"""  
  
 
