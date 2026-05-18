# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverseLL(head):
            curr=head
            prev=None
            while curr is None:
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt
            return prev
        # l1=reverseLL(l1)
        # l2=reverseLL(l2)
        carry=0
        dummyNode=ListNode(-1)
        curr=dummyNode
        while l1 is not None or l2 is not None or carry !=0:
            sum=carry
            if l1 is not None:
                sum+=l1.val
                l1=l1.next
            if l2 is not None:
                sum+=l2.val
                l2=l2.next
            curr.next= ListNode( sum%10)
            carry=0 if sum<10 else 1     
            curr=curr.next
        return dummyNode.next

