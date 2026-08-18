class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range((len(nums)) - 2):
            curr = nums[i]
            if curr > 0:
                break
            if curr == nums[i - 1] and i > 0:
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                if curr + nums[l] + nums[r] == 0:
                    res.append([curr, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif curr + nums[l] + nums[r] < 0:
                    l += 1 
                else:
                    r -= 1
        
        
        return res