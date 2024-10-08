def insert(head,data):
    new_node = Node(data)
    new_node.npx = id(head)  # npx of new node is current head's address
        
    if head is not None:
        # Update npx of current head
        head.npx = XOR(new_node, head.npx)

    return new_node  # Move head to point to new node

def getList(head):
    result_forward = []
    
    current = head
    prev_id = 0
        
    # Traverse forward
    while current is not None:
        result_forward.append(current.data)
        next_id = XOR(prev_id, current.npx)
        prev_id = id(current)
        current = None if next_id == 0 else next_id
        
    return result_forward
