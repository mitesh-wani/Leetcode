# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        greaterDummy =ListNode(0)
        lessDummy=ListNode(0)
        less = lessDummy
        greater = greaterDummy
        if head is None:
            return head
        curr=head
        while curr is not None:
            if curr.val>=x:
                greater.next=curr
                greater=greater.next
            else:
                less.next=curr  
                less=less.next 
            curr=curr.next
        greater.next=None
        less.next=greaterDummy.next
        return lessDummy.next       