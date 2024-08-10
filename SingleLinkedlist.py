# Creating a Node

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

#Creating Linked List
class LinkedList:
    def __init__(self):
        self.head = None
    
    def print(self):
        if self.head is None:
            print("Linked List is Empty")
            return 
        itr = self.head
        llstr = ' '

        while itr:
            # llstr += str(itr.data) + '----->' if itr.next else str(itr.data)
            llstr += str(itr.data) +( '----->' if itr.next else "")
            itr = itr.next

        print(llstr)

    #Traversing the Linked List
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        print(count)

ll = LinkedList()
#Nodes
ll.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

#combine three Nodes
ll.head.next = second
second.next = third
third.next = fourth

#Function Call
ll.print()
ll.get_length()