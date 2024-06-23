# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s=""
        
        n=head
        while n!=None:
            s+=str(n.val)
            n=n.next
           
        return int(s,2)
            
        