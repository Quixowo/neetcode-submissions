class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #use binary search: find high (nums[-1]) and low (nums[0]), compute middle

        high, low = len(nums) - 1 , 0

        while low <= high:
            mid = (high + low) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1 