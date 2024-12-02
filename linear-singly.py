def create_node(data):
    return {"data": data, "next": None}

def insert_at_beginning(head, data):
    new_node = create_node(data)
    new_node["next"] = head
    return new_node

def insert_at_end(head, data):
    new_node = create_node(data)
    if head is None:
        return new_node
    last_node = head
    while last_node["next"]:
        last_node = last_node["next"]
    last_node["next"] = new_node
    return head

def insert_at_middle(head, data, position):
    if position < 1:
        print("Invalid position!")
        return head
    new_node = create_node(data)
    if position == 1:
        new_node["next"] = head
        return new_node
    current = head
    for _ in range(position - 2):
        if current is None:
            print("Invalid position!")
            return head
        current = current["next"]
    if current is None:
        print("Invalid position!")
        return head
    new_node["next"] = current["next"]
    current["next"] = new_node
    return head

def delete_node(head, key):
    temp = head
    if temp is not None:
        if temp["data"] == key:
            head = temp["next"]
            return head
    while temp is not None:
        if temp["data"] == key:
            break
        prev = temp
        temp = temp["next"]
    if temp == None:
        return head
    prev["next"] = temp["next"]
    return head

def display(head):
    current = head
    while current:
        print(current["data"], end=" -> ")
        current = current["next"]
    print("None")

# Example usage:
if __name__ == "__main__":
    head = None
    for n in range(5):
        head = insert_at_beginning(head, n)
    print("Linked list:")
    display(head)

    head = delete_node(head, 3)
    print("\nAfter deleting node with data 3:")
    display(head)

    head = insert_at_beginning(head, 5)
    print("\nAfter inserting node with data 5 at the beginning:")
    display(head)

    head = insert_at_middle(head, 3, 2)
    print("\nAfter inserting node with data 3 at the middle position 2:")
    while head:
        print(head["data"], end=" -> ")
        head = head["next"]
    print("None")
