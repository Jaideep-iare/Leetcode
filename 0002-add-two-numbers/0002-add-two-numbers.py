# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1=""
        s2=""
        while l1!=None:
            s1=str(l1.val)+s1
            l1=l1.next

        while l2!=None:
            s2=str(l2.val)+s2
            l2=l2.next

        a=[int(i) for i in reversed(str(int(s1)+int(s2)))]
       
        head = ListNode(0)
        n=head
        for i in a:
            n.next = ListNode(i)
            n = n.next

        return head.next