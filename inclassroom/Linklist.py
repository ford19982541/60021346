class Node :
    dara =None 
    nextNode = None
    
    def __init__(self,data = None,nextNode = None):
        self.data =data
        self.nextNode = None


class LinkList :
    head = None

    def __init__(self,head = None) :
        self.head = head 

L = LinkList ()
node1 = Node(75)
node2 = Node(80)
node3 = Node(95)
node4 = Node(30)
node5 = Node(45)
 
L.head = node1
node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4
node4.nextNode = node5