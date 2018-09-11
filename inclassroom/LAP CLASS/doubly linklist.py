class Node :
    data =None 
    Next = None
    prev =None
    def __init__(self,data = None):
        self.data = data
        self.Next = None
        self.prev = None
        
class LinkList :
    head = None

    def __init__(self,head = None) :
        self.head = head 
    
    def Traversal(self): #print Node
        tmp = self.head
        while tmp:
            print(tmp.data)
            tmp =tmp.Next

    def additemLast(self,item): #add node
        if self.head is None :
            newNode = Node(item)
            newNode.prev =None
            self.head = newNode
        else:
            newNode = Node(item)
            cur = self.head
            while cur.Next :
                cur = cur.Next
            cur.Next = newNode
            newNode.prev = cur
            newNode.Next = None
            
    def deleteNode(self,key):
        if self.head == None:
            pass
        elif self.head.data == key:
            tmp = self.head
            self.head =self.head.Next
            self.head.prev = None
            del tmp
        else:
            cur = self.head
            prev =None
            
            while cur != None and cur.data != key :
                prev =cur
                cur = cur.Next
                
            if cur == None :
                print("cannot Delete")
                return
            prev.Next = cur.Next
            cur.Next = prev.Next
            del cur    
            
    def addfirst(self, data):
        if self.head is None:
            newNode = Node(data)
            newNode.Next = self.head
            self.head = newNode

        else:
            newNode = Node(data)
            self.head.prev = newNode
            newNode.Next = self.head
            self.head = newNode
            
            
    def addBefore(self,key,itemToInsert):
        cur=self.head
        prev=None
        while cur!=None and cur.data!=key:
            prev=cur
            cur=cur.Next
        
        if cur==self.head:
            self.additemLast(itemToInsert)
        elif(cur!=None):
            newNode=Node(itemToInsert)
            newNode.Next=cur
            prev.Next=newNode
            
    def addAfter(self,key,itemToInsert):
         prev=self.head
         cur=None
         while prev!=None and prev.data!=key:
            cur=prev
            prev=prev.Next
        
         if prev==self.head:
             self.additemLast(itemToInsert)
         elif(prev!=None):
            newNode=Node(itemToInsert)
            newNode.Next=prev
            cur.Next=newNode

L = LinkList ()
L.additemLast(21515)
L.additemLast(262256)
L.additemLast(2654941)
L.additemLast(1654)
L.additemLast(1)

L.addBefore(1654,56)
L.addAfter(1654,32)
L.deleteNode(1654)
L.addfirst(8)
L.addfirst(8)
L.Traversal()