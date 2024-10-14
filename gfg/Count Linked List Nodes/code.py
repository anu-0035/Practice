
#User function Template for python3

'''

#Linked list class
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        '''
class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head):
        # code here
        ans = 0 
        t = head
        while t:
            ans += 1
            t = t.next
        return ans
