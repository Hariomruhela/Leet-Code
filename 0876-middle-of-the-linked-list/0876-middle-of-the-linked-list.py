# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        count=0
        while(temp!=None):
            count=count+1
            temp=temp.next
        midle=(count//2)+1
        temp=head
        while(temp!=None):
            midle=midle-1
            if(midle==0):
                return temp    
            temp=temp.next
        return temp    