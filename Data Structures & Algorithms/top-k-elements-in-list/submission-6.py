class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        buckets = [[] for _ in range(len(nums) + 1)]
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num, freq in freq.items():
            buckets[freq].append(num)
        
        for i in range(len(nums), 0, -1):
            while buckets[i]:
                res.append(buckets[i].pop())
                if len(res) == k:
                    return res
            