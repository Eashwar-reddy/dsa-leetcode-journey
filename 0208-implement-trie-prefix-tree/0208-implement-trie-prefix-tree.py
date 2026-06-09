class Node:
    def __init__(self):
        self.links={}
        self.flag=False
    def contains(self,key):
        return key in self.links
    def put(self,key,node):
        self.links[key]=node
    def get(self,key):
        return self.links[key]
    def setEnd(self):
        self.flag=True
    def isEnd(self):
        return self.flag
class Trie(object):
    def __init__(self):
        self.root=Node()
    def insert(self, word):
        node=self.root
        for ch in word:
            if(not node.contains(ch)):
                node.put(ch,Node())
            node=node.get(ch)
        node.setEnd()
    def search(self, word):
        node=self.root
        for ch in word:
            if(not node.contains(ch)):
                return False
            node=node.get(ch)
        return node.isEnd()
    def startsWith(self, prefix):
        node=self.root
        for ch in prefix:
            if(not node.contains(ch)):
                return False
            node=node.get(ch)
        return True
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)