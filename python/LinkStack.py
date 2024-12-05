class LinkNode:                         
    def __init__(self,data=None):       
        self.data=data                  
        self.next=None                  
class LinkStack:                         
    def __init__(self):                 
        self.head=LinkNode()            
        self.head.next=None
    def empty(self):
        if self.head.next==None:
            return True
        return False
    def push(self,e):
        p=LinkNode(e)
        p.next=self.head.next
        self.head.next=p
    def pop(self):
        assert self.head.next!=None
        p=self.head.next
        self.head.next=p.next
        return p.data
    def geetop(self):
        assert self.head.next!=None
        return self.head.next.data
