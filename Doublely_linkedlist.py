class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_begin(self, data):
        new_node = Node(data)

        if self.head:
            self.head.prev = new_node
            new_node.next = self.head

        self.head = new_node

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # Insert at a specific position (1-based indexing)
    def insert_pos(self, pos, data):
        if pos < 1:
            print("Invalid Position")
            return

        new_node = Node(data)

        if pos == 1:
            new_node.next = self.head

            if self.head:
                self.head.prev = new_node

            self.head = new_node
            return

        temp = self.head

        for _ in range(pos - 2):
            if temp is None:
                print("Invalid Position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid Position")
            return

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next:
            temp.next.prev = new_node

        temp.next = new_node

    # Delete from beginning
    def delete_begin(self):
        if self.head is None:
            print("List is Empty")
            return

        self.head = self.head.next

        if self.head:
            self.head.prev = None

    # Delete from end
    def delete_end(self):
        if self.head is None:
            print("List is Empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.prev.next = None

    # Delete from a specific position
    def delete_pos(self, pos):
        if self.head is None:
            print("List is Empty")
            return

        if pos < 1:
            print("Invalid Position")
            return

        if pos == 1:
            self.head = self.head.next

            if self.head:
                self.head.prev = None
            return

        temp = self.head

        for _ in range(pos - 1):
            if temp is None:
                print("Invalid Position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid Position")
            return

        temp.prev.next = temp.next

        if temp.next:
            temp.next.prev = temp.prev

    # Search an element
    def search(self, key):
        temp = self.head
        pos = 1

        while temp:
            if temp.data == key:
                return pos

            temp = temp.next
            pos += 1

        return -1

    # Update an element
    def update(self, old_value, new_value):
        temp = self.head

        while temp:
            if temp.data == old_value:
                temp.data = new_value
                print("Value Updated")
                return

            temp = temp.next

        print("Value Not Found")

    # Display list
    def display(self):
        if self.head is None:
            print("NULL")
            return

        temp = self.head

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("NULL")

dll = DoublyLinkedList()

# Insert at beginning
dll.insert_begin(30)
dll.insert_begin(20)
dll.insert_begin(10)

# Insert at end
dll.insert_end(40)
dll.insert_end(50)

print("Original List:")
dll.display()

# Insert at position
dll.insert_pos(3, 25)

print("\nAfter Inserting 25 at Position 3:")
dll.display()

# Search
key = 40
position = dll.search(key)

if position != -1:
    print(f"\n{key} found at position {position}")
else:
    print(f"\n{key} not found")

# Update
dll.update(25, 26)

print("\nAfter Updating 25 to 26:")
dll.display()

# Delete from beginning
dll.delete_begin()

print("\nAfter Delete Begin:")
dll.display()

# Delete from end
dll.delete_end()

print("\nAfter Delete End:")
dll.display()

# Delete from position
dll.delete_pos(3)

print("\nAfter Delete Position 3:")
dll.display()
