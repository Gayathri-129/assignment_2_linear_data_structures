
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_linked_list(head, size):
    current = head
    prev = None
    next = None

    for _ in range(size):
        if current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

    if next is not None:
        head.next = reverse_linked_list(next, size)

    return prev


def create_linked_list(data):
    head = Node(data[0])
    prev = head
    for i in range(1, len(data)):
        node = Node(data[i])
        prev.next = node
        prev = node
    return head


def print_linked_list(head):
    node = head
    while node is not None:
        print(node.data)
        node = node.next


data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
size = 3
head = create_linked_list(data)
reversed_head = reverse_linked_list(head, size)
print_linked_list(reversed_head)