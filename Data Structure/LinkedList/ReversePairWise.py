#Reverse Pair iteratively

class Node:
    #Initialize the Node
    def __init__(self,data):
        self.data=data
        self.next=None

            



class LinkedList:
    #Initialize the  head with Null
    def __init__(self):
        self.head=None

    #Append at the Last
    def append(self,data):
        new_node = Node(data)

        #If LinkedList is Empty
        if self.head is None:
            self.head=new_node
            return


        last=self.head
        #Iterate to last of LinkedList
        while(last.next):
            last=last.next

        last.next=new_node



    #Function to Print the List
    def printList(self):
        temp=self.head
        print("Linked List is: ")
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next
            

    #Function to Reverse List PairWise
    def reversePairWise(self):
       #Intialize the variable
        temp1= temp2 = current = LinkedList()

       #initailize value of current
        current, temp1 ,temp2 = self.head, None , None

        while(current is not None and current.next is not None):
            if temp1 is not None:
                temp1.next.next=current.next

            temp1=current.next
            current.next=current.next.next
            temp1.next=current

            if temp2 is None:                
                temp2=temp1

            current=current.next

        #Changing the head to new list
        self.head=temp2
        

#Driver Code            
if __name__ == '__main__':
    
    #Initialize the Linked List
    llist=llist2 = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.append(4)
    
    llist.printList()
    print("\n")
    llist.reversePairWise()
    llist.printList()    
