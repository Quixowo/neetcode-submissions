# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        copy = head
        N = 0

        while copy:
            N += 1
            copy = copy.next
        
        from_front = N - n
        if from_front == 0:
            return head.next

        copy = head
        for i in range(N + 1):
            if (i + 1) == from_front:
                copy.next = copy.next.next
                break
            else:
                copy = copy.next

        return head