class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negated_nums = [-num for num in nums]

        heapq.heapify(negated_nums)
        while k > 1:
            heapq.heappop(negated_nums)
            k -= 1

        return -heapq.heappop(negated_nums)