class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def has_loop(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    
    return False

# Test: Create linked list with loop
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = head.next  # Create loop

if has_loop(head):
    print("Loop detected in linked list")
else:
    print("No loop in linked list")

# Test: Create linked list without loop
head2 = Node(1)
head2.next = Node(2)
head2.next.next = Node(3)

if has_loop(head2):
    print("Loop detected in linked list")
else:
    print("No loop in linked list")
