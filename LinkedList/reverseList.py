class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None
        
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def reverseLinkedList(self):
    
        current = self.head                    #head
        nxt = None                             
        prev = None
        while(current):
            nxt = current.next                #nxt = second
            current.next = prev               #current.next = None
            prev = current                    #prev = head
            current = nxt                     #current = second
            
        self.head = prev
        self.printlist()


        
         
        
        
                
        

if __name__ == '__main__':
    
    llist = Linkedlist()
    
    llist.head = Node(5)
    second = Node(6)
    third = Node(7)
    fourth = Node(7)
    fifth = Node(7)
    sixth = Node(10)
    seven = Node(11)
    eight = Node(11)
    
    llist.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    sixth.next = seven
    seven.next = eight

    llist.reverseLinkedList()