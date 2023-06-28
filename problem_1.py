class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def delete_zero_sum(self):
        current = self.head
        sum_dict = {}
        cumulative_sum = 0

        while current:
            cumulative_sum += current.data
            if cumulative_sum == 0:
                self.head = current.next
                current = self.head
                sum_dict = {}
                cumulative_sum = 0
            elif cumulative_sum in sum_dict:
                sum_dict[cumulative_sum].next = current.next
                current = current.next
                sum_dict = {}
                cumulative_sum = 0
            else:
                sum_dict[cumulative_sum] = current
                current = current.next


linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(12)
linked_list.insert(-12)
linked_list.insert(10)

print("Original Linked List:")
linked_list.display()

linked_list.delete_zero_sum()

print("Linked List after deleting zero-sum elements:")
linked_list.display()