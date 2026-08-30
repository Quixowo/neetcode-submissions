class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid

            #left half sorted
            if nums[l] <= nums[mid]:
                # check if target is in this portion; either greater than l or less than mid
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                #left portion is unsorted
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    # num not in this portion
                    l = mid + 1
            
        return -1