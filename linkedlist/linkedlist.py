class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    #display the linkedlist
    def display(self):
        if not self.head:
            print("Linkedlist is empty!")
            return
        temp = self.head
        while temp:
            print(temp.data, end = " -> ")
            temp = temp.next
        print("None")
    
    #insertion at a particular point in linkedlist
    def insertion(self,data,x):
        temp = self.head
        while temp:
            if temp.data == x:
                break
            temp = temp.next
        if temp:
            new_node = Node(data)
            new_node.next = temp.next
            temp.next = new_node
        else:
            print(f"Not found the value {x} in the linkedlist")
    
    #insertion at begin
    def insertion_begin(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    
    #insertion at the end
    def insertion_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    #searching
    def searching(self,x):
        if not self.head:
            print("Linkedlist is empty!")
            return
        temp = self.head
        while temp:
            if temp.data == x:
                print(f"{x} is in the linkedlist.")
                return
            temp = temp.next
        print(f"{x} is not in the linkedlist.")

    #reversing
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    #deletion at begin
    def deletion_begin(self):
        if not self.head:
            print("Empty linkedlist!")
            return
        self.head = self.head.next
    
    #deletion at end
    def deletion_end(self):
        if not self.head:
            print("Empty linkedlist!")
            return
        if not self.head.next:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp = None
    
    # deletion 
    def deletion(self,x):
        if not self.head:
            print("Empty linkedlist!")
            return
        if self.head.data == x:
            self.head = self.head.next
            return
        temp = self.head
        while temp.next:
            if temp.next.data == x:
                temp.next = temp.next.next
                return
            temp = temp.next
        print(f"Value of node {x} not found in the linkedlist")

    #length of linked list
    def length(self):
        if not self.head:
            print("Empty linkedlist!")
            return
        temp = self.head
        x = 0
        while temp :
            x += 1
            temp = temp.next
        print(f"Length of linkedlist is {x}")

def main():
    # Create a new Linkedlist object
    linked_list = Linkedlist()

    # Insert elements at the beginning
    linked_list.insertion_begin(10)
    linked_list.insertion_begin(20)
    linked_list.insertion_begin(30)

    # Insert elements at the end
    linked_list.insertion_end(40)
    linked_list.insertion_end(50)

    # Insert element after a specific value
    linked_list.insertion(25, 20)
    linked_list.insertion(35, 30)

    # Display the linked list
    print("Linked List after insertions:")
    linked_list.display()

    # Search for elements
    linked_list.searching(25)
    linked_list.searching(100)

    # Get the length of the linked list
    linked_list.length()

    # Reverse the linked list
    linked_list.reverse()
    print("Linked List after reversing:")
    linked_list.display()

    # Delete the first element
    linked_list.deletion_begin()
    print("Linked List after deletion at the beginning:")
    linked_list.display()

    # Delete the last element
    linked_list.deletion_end()
    print("Linked List after deletion at the end:")
    linked_list.display()

    # Delete a specific element
    linked_list.deletion(25)
    print("Linked List after deleting value 25:")
    linked_list.display()

    # Display final length
    linked_list.length()

if __name__ == "__main__":
    main()




         
        
                
        
        



    
        
            
                
                
    