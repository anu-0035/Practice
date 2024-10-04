#User function Template for python3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    # Function to reverse a circular linked list
    def reverse(self, head):
        #code here
        if not head or head.next == head:
            return head
        prev, curr, first = None, head, head
        
        while True:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            if curr == first:
                break
        head.next = prev
        head = prev
        
        return head
        
    # Function to delete a node from the circular linked list
    def deleteNode(self, head, key):
        #code here
        if not head:
            return None
        curr = head
        prev = None
        
        if head.data == key:
            if head.next == head:
                return None
            last = head
            while last.next != head:
                last = last.next
            last.next = head.next
            head = head.next
            return head
        
        prev = curr
        curr = curr.next
        while curr != head:
            if curr.data == key:
                prev.next = curr.next
                return head
            prev = curr
            curr = curr.next
        
        return head
