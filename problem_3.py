class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def create_linked_list(data):
    head = None
    for i in data:
        node = Node(i)
        if head is None:
            head = node
        else:
            prev_node.next = node
        prev_node = node
    return head


def merge_linked_lists(head1, head2):
    prev_node1 = head1
    prev_node2 = head2
    while prev_node1 and prev_node2:
        new_node = Node(prev_node2.data)
        new_node.next = prev_node1.next
        prev_node1.next = new_node
        prev_node1 = prev_node1.next.next
        prev_node2 = prev_node2.next
    return head1


def print_linked_list(head):
    node = head
    while node:
        print(node.data, end=" ")
        node = node.next


data1 = [1, 2, 3, 4, 5]
data2 = [6, 7, 8, 9, 10]

head1 = create_linked_list(data1)
head2 = create_linked_list(data2)

merged_list = merge_linked_lists(head1, head2)

print_linked_list(merged_list)