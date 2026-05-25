# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # time:O(2*(m+n)) space:O(1)
        # m,n=0,0
        # temp1,temp2=headA,headB
        # while temp1:
        #     m+=1
        #     temp1=temp1.next
        # while temp2:
        #     n+=1
        #     temp2=temp2.next
        # temp1,temp2=headA,headB
        # if m>n:
        #     for _ in range(m - n):
        #         temp1=temp1.next
        # else:
        #     for _ in range(n - m):
        #         temp2=temp2.next
        # while temp1 and temp2:
        #     if temp1==temp2:
        #         return temp1
        #     temp1=temp1.next
        #     temp2=temp2.next
        # return None

        # best optimal solution time:O(m+n) space:O(1)
        temp1,temp2=headA,headB
        while temp1!=temp2:
            temp1=temp1.next
            temp2=temp2.next
            if temp1==temp2:
                return temp1
            if temp1 is None:
                temp1=headB
            if temp2 is None:
                temp2=headA
        return temp1