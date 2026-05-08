# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        arr=[]
        temp=head
        while(temp!=None):
            arr.append(temp.val)
            temp=temp.next
        arr.reverse()
        i=0
        temp=head
        while(temp!=None):
            temp.val=arr[i]
            i+=1
            temp=temp.next
        return head