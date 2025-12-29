#define a static array
class StacticArray:
    def __init__(self,capacity):
        self.data=[0]*capacity
        self.capacity=capacity
        self.size=0

#operations of static array
    def append(self,val):
        if self.size>=self.capacity:
          raise Exception("数组满了")
        self.data[self.size]=val
        self.size += 1

    def insert(self,index,val):
        if index>self.size or index < 0:
            raise Exception("位置错误")
        elif self.size>=self.capacity:
            raise Exception("数组满了")
        else:
            for i in range(self.size-1,index-1,-1):
              self.data[i+1]=self.data[i]
            self.data[index]=val
            self.size += 1  

    def pop(self):
        if self.size==0:
          raise Exception("空数组")
        else:
          self.data[self.size-1]=0
          self.size-=1
    
    def remove(self,index):
       if self.size==0:
          raise Exception("空数组")
       elif index < 0 or index >= self.size:
          raise Exception("位置错误")
       else:
          for i in range(index,self.size-1):
             self.data[i]=self.data[i+1]
          self.data[self.size-1]=0
          self.size-=1

    def print_array(self):
        print(f"当前数组为：{self.data[:self.size]}")

#define a dynamic array
  

if __name__=="__main__":
    arr=StacticArray(10)
    arr.append(99)
    arr.print_array()
    arr.append(1)
    arr.print_array()
    arr.insert(0,3)
    arr.print_array()
    arr.pop()
    arr.print_array()
    arr.remove(1)
    arr.print_array()
    arr.remove(0)
    arr.print_array() 

    
        




      