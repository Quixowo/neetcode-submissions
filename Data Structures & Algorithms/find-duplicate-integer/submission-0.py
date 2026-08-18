class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashSet = set()

        p = nums
        for i in p:
            if i in hashSet:
                return i
            else:
                hashSet.add(i)
