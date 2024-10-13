#User function Template for python3

'''class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  
        self.next = None'''

class Solution:
    def deleteAlt(self, head):
        # code here
        if not head: return None
        cur = head
        while cur and cur.next:
            cur.next = cur.next.next
            cur = cur.next
        return head
