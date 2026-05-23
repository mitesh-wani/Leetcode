# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if head is None:
            return 0
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            
        back=None
        curr=slow
        while curr is not None:
            nxt=curr.next
            curr.next=back
            back=curr
            curr=nxt
        start=head
        end=back
        maxSum=0
        while end is not None:
            twinSum=start.val+end.val
            maxSum=max(twinSum,maxSum)
            start=start.next
            end=end.next
        return maxSum
        