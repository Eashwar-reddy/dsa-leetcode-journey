class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        self.prev=None
class BrowserHistory(object):

    def __init__(self, homepage):
        self.head=Node(homepage)
        self.temp=self.head
    def visit(self, url):
        self.temp.next=None
        newnode=Node(url)
        newnode.prev=self.temp
        self.temp.next=newnode
        self.temp=self.temp.next

    def back(self, steps):
        while(steps>0 and self.temp.prev!=None):
            steps-=1
            self.temp=self.temp.prev
        return self.temp.val
    def forward(self, steps):
        while(steps>0 and self.temp.next!=None):
            steps-=1
            self.temp=self.temp.next
        return self.temp.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)