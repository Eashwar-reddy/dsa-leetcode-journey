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
class WordDictionary(object):
    def __init__(self):
        self.root=Node()
    def addWord(self, word):
        node=self.root
        for ch in word:
            if(not node.contains(ch)):
                node.put(ch,Node())
            node=node.get(ch)
        node.setEnd()
    def search(self, word):
        return self.dfs(word,0,self.root)
    def dfs(self,word,idx,node):
        if(idx==len(word)):
            return node.isEnd()
        ch=word[idx]
        if(ch=='.'):
            for i in node.links.values():
                if(self.dfs(word,idx+1,i)):
                    return True
            return False
        else:
            if(not node.contains(ch)):
                return False
            return self.dfs(word,idx+1,node.get(ch))

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)