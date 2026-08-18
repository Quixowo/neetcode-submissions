class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(0, len(nums) - 2):
            curr = nums[i]

            if curr > 0:
                break
            if i > 0 and curr == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = curr + nums[l] + nums[r]
                if threeSum == 0:
                    res.append([curr, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                elif threeSum < 0:
                    l += 1
                else:
                    r -= 1
            
        return res