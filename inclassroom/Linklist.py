class Node :
    data =None 
    nextNode = None
    
    def __init__(self,data = None,nextNode = None):
        self.data = data
        self.nextNode = None


class LinkList :
    head = None

    def __init__(self,head = None) :
        self.head = head 
        #add node
    def additem(self,item):
        newNode = Node(item)
        newNode.nextNode = self.head
        self.head = newNode
    def Traversal(self):
        tmp = self.head
        while(tmp != None):
            print(tmp.data)
            tmp =tmp.nextNode
            
    def insertAfter(self,key,itemToinsert):
        tmp =self.head
        while(tmp != None and tmp.data != key):
            tmp = tmp.nextNode
        
        if(tmp != None):
            newNode = Node(itemToinsert)
            newNode.nextNode = tmp.nextNode
            tmp.nextNode =newNode
            
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
'''
temp = L.head

print(temp.data)
while (temp.nextNode != None):
    temp = temp.nextNode
    print(temp.data)
    
temp = L.head
while (temp != None):
    print(temp.data)
    temp = temp.nextNode

#print Node
def printrecru(temp):
    if (temp == None):
        pass
    else :
        print(temp.data)
        printrecru(temp.nextNode)
        
        '''
L.additem(12)
L.insertAfter(80,5)
L.insertAfter(45,40)
L.Traversal()



