

# Node class


class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# Linked List class
class LinkedList:

    def __init__(self):
        self.head = None

    def createList(self, arr):
        start = self.head
        n = len(arr)
        # Declare newNode and temporary pointer
        temp = start
        i = 0

        # Iterate the loop until array length
        while (i < n):

            # Create new node
            newNode = Node(arr[i])

            if (i == 0):
                start = newNode
                newNode.prev = start
                temp = start

            else:
                temp.next = newNode
                newNode.prev = temp
                temp = temp.next
            i = i + 1
        self.head = start
        return start

    def printList(self):
        temp = self.head
        linked_list = ""
        while(temp):
            linked_list += (str(temp.data) + " ")
            temp = temp.next
        print(linked_list)

    # Function to count nunmber of
    # elements in the list

    def countList(self):

        # Declare temp pointer to
        # traverse the list
        temp = self.head

        # Variable to store the count
        count = 0

        # Iterate the list and increment the count
        while (temp is not None):
            temp = temp.next
            count = count + 1

        return count

    # we will consider that the index begin at 1
    def deleteAtLocation(self, index):
      temp = self.head

      count = self.countList()

      if(count < index):
        return temp

      if(index == 1):
        temp = temp.next
        self.head = temp
        return self.head

      if(count == index):
        while(temp.next is not None and temp.next.next is not None):
          temp = temp.next
         # 1 => 2 => 3 => 4
        temp.next = None
        return self.head
      

      i = 1 
      while(i<index-1):
        temp = temp.next
        i+=1
      

      prevNode = temp
      nodeAtTarget = temp.next
      nextNode = nodeAtTarget.next

      # 1 => 2 => 3 => 4

      nextNode.prev = prevNode
      prevNode.next = nextNode

      return self.head

        
# create an empty list

arr = [1, 2, 3, 4, 5]
llist = LinkedList()

llist.createList(arr)


llist.deleteAtLocation(2)

# print(llist.head)
llist.printList()
