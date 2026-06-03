# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq as hp
class Solution(object):
    def mergeKLists(self, lists):
        heap=[]
        for i in lists:
            if(i):
                hp.heappush(heap,[i.val,i])
        dummy=ListNode(-1)
        temp=dummy
        while(heap!=[]):
            l=hp.heappop(heap)
            node=l[1]
            temp.next=node
            temp=temp.next
            node=node.next
            if(node):
                hp.heappush(heap,[node.val,node])
        return dummy.next
