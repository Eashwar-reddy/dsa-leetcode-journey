class Node:
    def __init__(self):
        self.links={}
        self.flag=False
    def contains(self,ch):
        return ch in self.links
    def setEnd(self):
        self.flag=True
    def isEnd(self):
        return self.flag
    def put(self,ch,node):
        self.links[ch]=node
    def get(self,ch):
        return self.links[ch]
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
        node=self.root
        for ch in word:
            if(node.get(ch).isEnd()):
                node=self.root
                continue
            if(not node.contains(ch)):
                return False
            node=node.get(ch)
        return True
class Solution(object):
    def wordBreak(self, s, wordDict):
        trie=Trie()
        for i in wordDict:
            trie.insert(i)
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True  
        for i in range(n):
            if not dp[i]:  
                continue
            node=trie.root
            for j in range(i,n):
                ch=s[j]
                if not node.contains(ch):
                    break         
                node = node.get(ch)
                if node.isEnd():
                    dp[j + 1] = True 

        return dp[n]