class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums) - 2):
            curr = nums[i]
            l, r = i + 1, len(nums) - 1

            if curr > 0:
                break
            if nums[i - 1] == curr and i > 0:
                continue

            while l < r:
                threeSum = curr + nums[l] + nums[r]
                if threeSum == 0:
                    res.append([curr, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif threeSum < 0:
                    l += 1
                else:
                    r -= 1

        return res