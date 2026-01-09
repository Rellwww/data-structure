from collections import deque

# Implementation of a Queue
class MyQueue:
    def __init__(self):
        # Using deque (double-ended queue) for storage
        self.list = deque()

    # Insert element at the rear (Enqueue)
    # Time Complexity: O(1)
    def push(self, element):
        self.list.append(element)

    # Remove element from the front (Dequeue)
    # Time Complexity: O(1)
    def pop(self):
        return self.list.popleft()

    # Peek at the front element (without removing)
    # Time Complexity: O(1)
    def peek(self):
        return self.list[0]

    # Return the number of elements
    # Time Complexity: O(1)
    def size(self):
        return len(self.list)

# Implementation of a Stack
class MyStack:
    def __init__(self):
        self.list = deque()

    # Insert element at the top (Push)
    # Time Complexity: O(1)
    def push(self, element):
        self.list.append(element)

    # Remove element from the top (Pop)
    # Time Complexity: O(1)
    def pop(self):
        return self.list.pop()

    # Peek at the top element (without removing)
    # Time Complexity: O(1)
    def peek(self):
        return self.list[-1]

    # Return the number of elements
    # Time Complexity: O(1)
    def size(self):
        return len(self.list)

if __name__ == "__main__":
    # Test Queue
    print("--- Testing Queue ---")
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    print(f"Peek front: {queue.peek()}")  # Should be 1
    print(f"Pop front: {queue.pop()}")    # Should be 1
    print(f"Pop front: {queue.pop()}")    # Should be 2
    print(f"Peek front: {queue.peek()}")  # Should be 3
    print(f"Queue size: {queue.size()}")  # Should be 1

    # Test Stack
    print("\n--- Testing Stack ---")
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Peek top: {stack.peek()}")    # Should be 3
    print(f"Pop top: {stack.pop()}")      # Should be 3
    print(f"Pop top: {stack.pop()}")      # Should be 2
    print(f"Peek top: {stack.peek()}")    # Should be 1
    print(f"Stack size: {stack.size()}")  # Should be 1