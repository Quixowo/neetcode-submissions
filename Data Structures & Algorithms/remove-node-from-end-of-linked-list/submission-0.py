# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        node = head

        while node:
            N += 1
            node = node.next

        from_front = N - n

        if from_front == 0: return head.next

        node = head
        for i in range(N - 1):
            if (i + 1) == from_front:
                node.next = node.next.next
                break
            else: 
                node = node.next 
        return head
