# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans = []
        t1 = head
        n = 0
        while t1:
            n +=1
            t1 = t1.next
        part,left = n//k,n%k
        t1,prev = head,None
        for _ in range(k):
            ans.append(t1)
            for _ in range(part):
                if t1:
                    prev = t1
                    t1 = t1.next
            if left and t1:
                prev = t1
                t1 = t1.next
                left -= 1
            if prev: prev.next = None
        return ans 
                


        
