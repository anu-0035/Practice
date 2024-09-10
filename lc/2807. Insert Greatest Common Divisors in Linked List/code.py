# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        if not head or not head.next: return head
        prev=head
        curr=head.next
        while(curr!=None):
            temp=gcd(prev.val,curr.val)
            newnode=ListNode(val=temp)
            newnode.next=curr
            prev.next=newnode
            prev=curr
            curr=curr.next
        return head
        
