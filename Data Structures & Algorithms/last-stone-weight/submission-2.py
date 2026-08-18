class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        alt_stones = [-stone for stone in stones]

        #negate stone weight so heapify can do a max-heap
        heapq.heapify(alt_stones)

        while len(alt_stones) > 1:
            first_stone = -(heapq.heappop(alt_stones))
            second_stone = -(heapq.heappop(alt_stones))

            if first_stone < second_stone:
                heapq.heappush(alt_stones, -(second_stone - first_stone))
            elif second_stone < first_stone:
                heapq.heappush(alt_stones, -(first_stone - second_stone))
        
        return -alt_stones[0] if len(alt_stones) == 1 else 0


