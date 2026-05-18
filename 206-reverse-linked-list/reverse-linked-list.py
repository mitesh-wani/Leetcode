# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        back=None
        curr=head
        while curr is not None:
            nxt=curr.next
            curr.next=back
            back=curr
            curr=nxt
        return back
