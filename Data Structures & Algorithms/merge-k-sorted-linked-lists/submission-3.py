# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not list or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if len(lists) > (i + 1) else None

                mergedLists.append(self.mergeList(l1, l2))
            
            lists = mergedLists

        return lists[0]
        
    def mergeList(self, list1, list2):
        dummy = ListNode()
        copy = dummy

        while list1 and list2:
            if list1.val < list2.val:
                copy.next = list1
                list1 = list1.next
            else:
                copy.next = list2
                list2 = list2.next
            copy = copy.next

        if list1:
            copy.next = list1
        if list2:
            copy.next = list2


        return dummy.next