from collections import deque
#队列的实现
class Myqueue:
  def __init__(self):
    self.list=deque()
  #队尾插入元素 时间复杂度O(1)
  def push(self,element):
    self.list.append(element)
  #队头删除元素，时间复杂度O(1)
  def pop(self):
    return self.list.popleft()
  #查看队头元素，时间复杂度O(1)
  def peek(self):
    return self.list[0]
  #返回元素个数，时间复杂度O(1)
  def size(self):
    return len(self.list)
#栈的实现
class Mystack:
  def __init__(self):
    self.list=deque()
  #栈顶插入元素，时间复杂度O(1)
  def push(self,element):
    self.list.append(element)
  #栈顶删除元素，时间复杂度O(1)
  def pop(self):
    return self.list.pop()
  #查看栈顶元素，时间复杂度O(1)
  def peek(self):
    return self.list[-1]
  #返回元素个数，时间复杂度O(1)
  def size(self):
    return len(self.list)

if __name__=="__main__":
  queue=Myqueue()
  queue.push(1)
  queue.push(2)
  queue.push(3)
  print(queue.peek())
  print(queue.pop())
  print(queue.pop())
  print(queue.peek())
  print(queue.size())
  stack=Mystack()
  stack.push(1)
  stack.push(2)
  stack.push(3)
  print(stack.peek())
  print(stack.pop())
  print(stack.pop())
  print(stack.peek())
  print(stack.size())



    

  