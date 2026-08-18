class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq = {}
        buckets = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        for num, freq in freq.items():
            buckets[freq].append(num)

        for i in range(len(nums), 0, -1):
            for elem in buckets[i]:
                res.append(elem)
                if len(res) == k:
                    return res

        