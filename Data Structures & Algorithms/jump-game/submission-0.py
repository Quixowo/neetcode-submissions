class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n - 1
        req = 1  # required number to jump successfully

        for i in range(n - 2, -1, -1):
            if nums[i] >= req:
                goal = i
                req = 1
            else:
                req += 1

        return goal == 0