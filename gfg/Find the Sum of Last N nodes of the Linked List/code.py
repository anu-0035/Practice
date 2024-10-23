#User function Template for python3

'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def sumOfLastN_Nodes(self, head, n):
        #function should return sum of last n nodes
        dummy = Node(0)
        dummy.next = head
        fast = slow = dummy
        for i in range(n):
            fast = fast.next
        s = 0
        while fast:
            slow = slow.next
            fast = fast.next
        
        while slow:
            s += slow.data
            slow = slow.next
        return s
