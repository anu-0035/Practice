
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1,h2 = l1,l2
        temp = ListNode(0) 
        cur = temp
        c = 0
        while  h1 or  h2:
            s = c
            if h1 != None:
                s += h1.val
                h1 = h1.next
            if h2 != None:
                s += h2.val
                h2 = h2.next
            cur.next = ListNode(s%10)
            c = s // 10
            cur = cur.next
        if c != 0:
            cur.next = ListNode(c)
        
        return temp.next
        
