# Creating a Node

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

#Creating Linked List
class LinkedList:

    #Creating Linked List
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
        return count

    #Insersion at Begining of linked List
    def Insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node

    #Insersion at End of Linked List
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data)
            return 
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)

    #Insersion at Perticular index of linked list
    def insert_at(self,index,data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index!")
            # return print("Invalid!")
        if index == 0:
            self.Insert_at_begining(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    
    #Deleting a Node at Begining
    def delete_at_begining(self):
        if not self.head:
            return None
        temp = self.head
        self.head = self.head.next
        temp = None


    #Deleting a Node at End
    def delete_at_end(self):
        if self.head is None:
            return None
        if self.head.next == None:
            self.head = None
            return 
        
        itr = self.head
        while itr.next.next:
            itr = itr.next
        itr.next = None



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

#1,2,3,4
# ll.print()

#length
# ll.get_length()

#insert 10 at start
ll.Insert_at_begining(10)

#Insert 5 at end
ll.insert_at_end(5)

#Insert data at particular Index
ll.insert_at(3,10)

# Delete Node at Begining
ll.delete_at_begining()

# Delete Node at Begining
ll.delete_at_end()
ll.print()