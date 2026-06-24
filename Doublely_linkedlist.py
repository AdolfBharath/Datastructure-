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

    def insertpos(self,pos,data):
        new_node = Node(data)
        if pos == 1:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return
        temp = self.head
        for i in range(pos-2):
            temp = temp.next
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node

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

    def deletepos(self,pos):
        if self.head is None:
            return
        if pos == 1:
            self.head = self.head.next 
            if self.head:
                self.head.prev = None
            return
        temp = self.head
        for i in range(pos-1):
            temp = temp.next
        temp.prev.next = temp.next
        if temp.next:
            temp.next.prev = temp.prev
            
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
