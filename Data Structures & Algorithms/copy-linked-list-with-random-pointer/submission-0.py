"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        toCopy = {None: None}
        p = head

        while p:
            copy = Node(p.val)
            toCopy[p] = copy
            p = p.next

        p = head
        while p:
            copy = toCopy[p]
            copy.next = toCopy[p.next]
            copy.random = toCopy[p.random]
            p = p.next

        return toCopy[head]
