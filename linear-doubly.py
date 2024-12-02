class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node
    def insert_at_middle(self, data, position):
        if position < 1:
            print("Invalid position!")
            return
        new_node = Node(data)
        if position == 1:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 2):
            if current is None:
                print("Invalid position!")
                return
            current = current.next
        if current is None:
            print("Invalid position!")
            return
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node
    def delete_node(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                if self.head:
                    self.head.prev = None
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            temp = temp.next
        if temp == None:
            return
        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next
        temp = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


# Example usage:
if __name__ == "__main__":
    linked_list = DoublyLinkedList()
    linked_list.insert_at_end(1)
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(3)
    linked_list.insert_at_end(4)
    print("Linked list:")
    linked_list.display()

    linked_list.delete_node(3)
    print("\nAfter deleting node with data 3:")
    linked_list.display()

    linked_list.insert_at_beginning(5)
    print("\nAfter inserting node with data 5 at the beginning:")
    linked_list.display()

    linked_list.insert_at_middle(3, 2)
    print("\nAfter inserting node with data 3 at the middle potition 2:")
    linked_list.display()
