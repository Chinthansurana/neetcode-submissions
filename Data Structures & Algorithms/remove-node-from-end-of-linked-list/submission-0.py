# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        cur = head
        while cur:
            N += 1
            cur = cur.next
        removeind = N-n
        if removeind == 0:
            return head.next
        
        cur = head
        for i in range(N-1):
            if (i+1) == removeind:
                cur.next = cur.next.next
                break
            cur = cur.next
        return head