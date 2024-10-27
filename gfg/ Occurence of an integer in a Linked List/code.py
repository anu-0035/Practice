"""  
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
class Solution:
    def count(self, head, key):
        # Code here
        count = 0
        t = head
        while t: 
            if t.data == key:
                count += 1
            t = t.next
        return count
