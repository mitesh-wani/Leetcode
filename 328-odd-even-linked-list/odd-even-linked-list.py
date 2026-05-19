# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None or head.next.next is None:
            return head
        odd=head
        even=head.next
        evenHead=head.next
        curr=head.next.next
        idx=1
        while curr is not None:
            nxtNode=curr.next # SAVE the next node before modifying anything!
            if idx%2==1:
                odd.next=curr
                odd=odd.next
            else:
                even.next=curr
                even=even.next
                
            curr=nxtNode
            idx+=1
        even.next = None #terminate the even list
        odd.next=evenHead
        return head
