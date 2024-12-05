class LinkNode:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class LinkQueue:
    def __init__(self):
        self.front=None
        self.rear=None
    def empty(self):
        return self.front==None
    def push(self,e):
        s=LinkNode(e)
        if self.empty():
            self.front=self.rear=s
        else:
            self.rear.next=s
            self.rear=s
    def pop(self):
        assert not self.empty()
        if self.front==self.rear:
            e=self.front.data
            self.front=self.rear=None
        else:
            e=self.front.data
            self.front=self.front.next
        return e
    def gethead(self):
        assert not self.empty()
        e=self.front.data
        return e
