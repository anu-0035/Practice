#User function Template for python3
'''
class DLLNode:
    def __init__(self,val) -> None:
        self.data = val
        self.prev = None
        self.next = None
'''
class Solution:
    def sortAKSortedDLL(self, head, k):
        # Code Here
        if not head : return None
        heap = []
        cur = head
        for  _ in range(k+1):
            heapq.heappush(heap,cur.data)
            cur = cur.next
        
        sorted_head = DLLNode(0)
        last = sorted_head
        
        while heap:
            smallest = DLLNode(heapq.heappop(heap))
            last.next = smallest
            smallest.prev = last
            last = smallest
            
            if cur:
                heapq.heappush(heap,cur.data)
                cur = cur.next
        last.next = None
        return sorted_head.next
            
