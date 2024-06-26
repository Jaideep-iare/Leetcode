# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1=""
        s2=""
        c1=0
        c2=0
        i=0
        while l1!=None:
            c1+=l1.val*10**i 
            i+=1
            l1=l1.next

        i=0
        while l2!=None:
            c2+=l2.val*10**i
            i+=1
            l2=l2.next


        a=reversed(str(c1+c2))

       
        head = ListNode(0)
        n=head
        for i in a:
            n.next = ListNode(i)
            n = n.next

        return head.next