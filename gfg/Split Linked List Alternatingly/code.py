#User function Template for python3
'''
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def alternatingSplitList(self, head):
        #Your code here
        cur = head
        t1,t2 = Node(0),Node(0)
        a1,a2 = t1,t2
        flag = True
        while cur:
            if flag : 
                t1.next = cur
                t1 = t1.next
            else : 
                t2.next = cur
                t2 = t2.next
            cur = cur.next
            flag = not flag
        t1.next = None
        t2.next = None
        return [a1.next,a2.next]
