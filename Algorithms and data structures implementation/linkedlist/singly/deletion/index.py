class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        linked_list = ""
        while(temp):
            linked_list += (str(temp.data) + " ")
            temp = temp.next
        print(linked_list)

    def deleteNode(self, key):
        temp = self.head
        if(temp is None):
            return
        if(temp.data == key):
            self.head = temp.next
            temp = None
            return

        while(temp.next.data != key):
            temp = temp.next

        target_node = temp.next
        temp.next = target_node.next
        target_node.next = None


# List Structure : 5 => 1 => 3 => 7
# 5 => 1 => 7
linked_list = LinkedList()
linked_list.head = Node(5)

second_node = Node(1)
third_node = Node(3)
fourth_node = Node(7)

linked_list.head.next = second_node
second_node.next = third_node
third_node.next = fourth_node

linked_list.deleteNode(3)
linked_list.printList()
