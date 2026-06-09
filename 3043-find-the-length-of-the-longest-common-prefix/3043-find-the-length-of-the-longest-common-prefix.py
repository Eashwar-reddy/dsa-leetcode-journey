class Node:
    def __init__(self):
        self.links={}
        self.flag=False
    def contains(self,ch):
        return ch in self.links
    def put(self,ch,node):
        self.links[ch]=node
    def get(self,ch):
        return self.links[ch]
    def isEnd(self):
        return self.flag
    def setEnd(self):
        self.flag=True
class Trie:
    def __init__(self):
        self.root=Node()
    def insert(self,word):
        node=self.root
        for ch in word:
            if(not node.contains(ch)):
                node.put(ch,Node())
            node=node.get(ch)
        node.setEnd()
    def search(self,word):
        self.count=0
        node=self.root
        for ch in word:
            if(not node.contains(ch)):
                return self.count
            self.count+=1
            node=node.get(ch)
        return self.count
class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        trie=Trie()
        for i in arr1:
            trie.insert(str(i))
        ans=0
        for i in arr2:
            ans=max(ans,trie.search(str(i)))
        return ans