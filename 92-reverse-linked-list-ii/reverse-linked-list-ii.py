# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None or head.next is None or left==right:
            return head

        back=None
        curr=head
        for _ in range(left-1):
            if curr is not None:
                back=curr
                curr=curr.next
# not understand neatly
        # for _ in range(right-left):
        #     front=curr.next
        #     curr.next=front.next
        #     front.next=prev.next
        #     prev.next=front
        toStart=back
        start=curr
        #print(back.val)
        prev=None
        
        for _ in range(right-left+1):
            if curr is not None:
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt
        start.next=curr
        if toStart is not None:
            toStart.next=prev
        else:
            return prev
        return head 

        

        