class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        points_tuple = [(math.sqrt(x**2 + y**2), [x, y]) for x, y in points]
        # [(2, [2, 2]), (2.82842, [2, 2])]

        heap = []
        for pair in points_tuple:
            heap.append(pair)

        heapq.heapify(heap)

        for _ in range(k):
            smallest_distance = heapq.heappop(heap)
            res.append(smallest_distance[1])

        return res