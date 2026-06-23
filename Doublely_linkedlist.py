class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class Doublelinked:
    def __init__(self):
        self.head = None

    def insertb(self, data):
        new_node = Node(data)

        if self.head:
            self.head.prev = new_node
            new_node.next = self.head

        self.head = new_node

    def inserte(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    def deleteb(self):
        if self.head is None:
            return

        self.head = self.head.next

        if self.head:
            self.head.prev = None

    def deletee(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.prev.next = None

    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("NULL")


dl = Doublelinked()

dl.insertb(35)
dl.insertb(30)
dl.insertb(20)
dl.insertb(10)

dl.inserte(40)
dl.inserte(45)

print("Original:")
dl.display()

dl.deletee()
dl.deleteb()

print("After Deletion:")
dl.display()
