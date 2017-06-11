#Creating the Linked List

#Declaring the Node
class Node:
    def __init__(self,data):        
        self.data=data
        self.next=None


class LinkedList:
    #Initializing head
    def __init__(self):
        self.head=None

    #Print the List
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next



if __name__ == "__main__":

    llist = LinkedList()

    #Creating the Nodes
    llist.head=Node(1)
    second=Node(2)
    third=Node(3)

    #Connecting the Nodes
    llist.head.next=second
    second.next=third
    print("Linked List is :",end=" ")
    llist.printList()







    
