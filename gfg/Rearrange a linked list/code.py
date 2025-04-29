#User function Template for python3

'''
# Linked List Node 
class Node: 
	def __init__(self, d): 
		self.data = d 
		self.next = None
		'''
class Solution:    
    def rearrangeEvenOdd(self, head):
        #code here
        if not head or not head.next:
            return head
        odd = head
        even = head.next
        even_head = even
        
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            
            even.next = odd.next
            even = even.next
        odd.next = even_head
        
        return head
