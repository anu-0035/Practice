class MyCircularDeque:

    def __init__(self, k: int):
        self.head = 0
        self.tail = 0
        self.size = 0
        self.k = k
        self.dq = [None] * k
        
    def insertFront(self, value: int) -> bool:
        if self.isFull() : return False
        self.head = (self.head - 1 +self.k) % self.k
        self.dq[self.head] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull() : return False
        self.dq[self.tail] = value
        self.size += 1
        self.tail = (self.tail + 1) % self.k
        return True

        

    def deleteFront(self) -> bool:
        if self.isEmpty() : return False
        self.head = (self.head +1) % self.k
        self.size -= 1
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty() : return False
        self.tail = (self.tail -1 + self.k) % self.k
        self.size -= 1
        return True

    def getFront(self) -> int:
        if not self.isEmpty() :
            return self.dq[self.head]
        return -1

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.dq[(self.tail -1 +self.k) % self.k]
        return -1
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool: 
        return self.size == self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
