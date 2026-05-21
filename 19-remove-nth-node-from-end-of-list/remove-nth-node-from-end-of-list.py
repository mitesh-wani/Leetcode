# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        if head.next is None and n==1:
            return None
        
        dummy = ListNode(0)
        dummy.next = head
        curr=dummy
        back=dummy
        for _ in range(n+1):
            curr=curr.next
        
        front=curr
        if front is None:
            return head.next
        nxt=head
        while front is not None :
            back=back.next
            front=front.next
            
        back.next=back.next.next
        return head
        