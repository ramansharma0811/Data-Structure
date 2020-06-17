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
    def removeDuplicate (self):
        current = self.head
        nxt = None
        while(current and current.next):
            nxt = current.next              
            if(current.data == nxt.data):
                current.next = nxt.next
            else:  
                current = current.next
        
        self.printlist()

        # 7/200   -->    7/300   -->  7/400   --> 10/none
       #   100            200          300         400  
       # 7/300   -->    7/400  -->  10/none
       # 100            300         400
       # 7/400  -->   10/none
       # 100            400


        
         
        
        
                
        

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

    llist.removeDuplicate()