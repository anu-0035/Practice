'''
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}'''
	
class Solution:
    def segregate(self, head):
        #code here
        count = [0,0,0]
        t = head
        while  t:
            count[t.data] += 1
            t = t.next
        
        t = head
        i = 0
        while t:
            if count[i] == 0:
                i += 1
            else:
                t.data = i
                count[i] -= 1
                t = t.next
        return head
