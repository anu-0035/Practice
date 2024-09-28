class MyCircularDeque:

    def __init__(self, k: int):
        self.head = 0
        self.tail = 0
        self.size = 0
        self.k = k
        self.dq = [None] * k
        
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.head = (self.head - 1 + self.k) % self.k  # Move head back
        self.dq[self.head] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.dq[self.tail] = value
        self.tail = (self.tail + 1) % self.k  # Move tail forward
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        # Remove the element at head position
        self.head = (self.head + 1) % self.k  # Move head forward
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        # Move tail back to remove the last element
        self.tail = (self.tail - 1 + self.k) % self.k  # Move tail back
        self.size -= 1
        return True

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.dq[self.head]
        return -1

    def getRear(self) -> int:
        if not self.isEmpty():
            # The last element is at (tail - 1 + k) % k
            return self.dq[(self.tail - 1 + self.k) % self.k]
        return -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k
    
  

def main():
    # Create a circular deque with a maximum size of 3
    k = 3
    deque = MyCircularDeque(k)

    # Test insertLast and check results
    print(deque.insertLast(1))   # True
    print(deque.insertLast(2))   # True
    print(deque.insertFront(3))  # True
    print(deque.insertFront(4))  # False (deque is full)

    # Check current state of the deque
    print("Front:", deque.getFront())  # Should return 3
    print("Rear:", deque.getRear())    # Should return 2

    # Check if the deque is full
    print(deque.isFull())              # True

    # Remove an element from the rear and check state
    print(deque.deleteLast())          # True
    print(deque.getRear())             # Should return 1 (after deleting 2)

    # Insert another element at the front
    print(deque.insertFront(4))        # True
    print(deque.getFront())             # Should return 4

    # Remove an element from the front and check state
    print(deque.deleteFront())         # True
    print(deque.getFront())            # Should return 3

    # Final checks for emptiness and fullness
    print(deque.isEmpty())             # False (should have elements)
    
    # Remove remaining elements to check empty state
    deque.deleteFront()                # Remove 3
    deque.deleteLast()                 # Remove 1
    
    print(deque.isEmpty())             # True (should be empty now)

# Run the main function to test the MyCircularDeque implementation
if __name__ == "__main__":
    main()


