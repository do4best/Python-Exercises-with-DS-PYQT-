class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,new_data):

        new_data = Node(new_data)
        new_data.next = self.head
        self.head = new_data

    def insertAfter(self,pre_node,new_data):
        if pre_node is None:
            print("The Given previous node must be in LinkedList")
            return
        new_node = Node(new_data)
        new_node.next = pre_node.next
        pre_node.next = new_data

    def append(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def printLL(self):

        temp = self.head
        while(temp):
            print(temp.data, end=' ')
            temp = temp.next


linked = LinkedList()
linked.head = Node(1)
second = Node(2)
third = Node(3)

linked.head.next = second
second.next = third
linked.push(5)
linked.push(6)
linked.append(1)
linked.insertAfter(2,10)
linked.printLL()