class Node:     #node 
    def __init__(self,data):
        self.data = data
        self.next = None
#this is cretaing linked list 
class Linkedlist:
# setting the head to null first 
    def __init__(self):
        self.head = None
# inserting the element in the beganing 
    def insertb(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head= new_node
# inserting the element at the last 
    def inserte(self,data):
        new_node = Node(data) 
# checking the head node is either null or not 
        if self.head is None:
            self.head = new_node
            return 
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
# deteling the element at the beganning
    def deleteb(self):
# checking the element is there at head (first) or not 
        if self.head is None:
            print("empty")
            return
        self.head=self.head.next
# deleting aat the last 
    def deletee(self):
        if self.head is None:
            print("empty")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head 
        while temp.next.next:
            temp = temp.next
        temp.next = None
            
        
    def display(self):
        temp = self.head
        while temp:
            print(temp.data,end="->")
            temp = temp.next
        print("null")
l = Linkedlist()
l.insertb(10)
l.insertb(20)
l.insertb(30)
l.inserte(35)
l.display()
l.deletee()
l.deleteb()
l.display()
