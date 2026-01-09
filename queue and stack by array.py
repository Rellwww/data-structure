#数组实现stack
class MyStack:
  def __init__(self):
    self.arr=[]
#向栈顶加入元素，时间复杂度O(1)
  def push(self,element):
    return self.arr.append(element)
#从栈顶弹出元素，时间复杂度 O(1)
  def pop(self):
    return self.arr.pop()
# 查看栈顶元素，时间复杂度 O(1)
  def peek(self):
    return self.arr[-1]
# 返回元素个数，时间复杂度 O(1)  
  def size(self):
    return len(self.arr)
  
#数组实现queue
class Myqueue:
  def __init__(self):
    self.arr=[]
#向队列前端加入元素，时间复杂度O(1)  
  def push(self,element):
    return self.arr.append(element)
#向队列后端加入元素，时间复杂度O(1)  
  def pop(self):
    if len(self.arr)==0:
      raise IndexError("No element in the queue")
    else:
      return self.arr.pop(0)
# Peek at the top element (without removing)
# Time Complexity: O(1)
  def peek(self):
    return self.arr[-1]
# Return the number of elements
# Time Complexity: O(1)
  def size(self):
    return len(self.arr)

if __name__=="__main__":
  stack=MyStack()
  stack.push(1)
  stack.push(2)
  stack.push(3)
  print(stack.peek())
  print(stack.pop())
  print(stack.pop())
  print(stack.peek())
  print(stack.size())
  queue=Myqueue()
  queue.push(1)
  queue.push(2)
  queue.push(3)
  print(queue.peek())
  print(queue.pop())
  print(queue.pop())
  print(queue.peek())
  print(queue.size())