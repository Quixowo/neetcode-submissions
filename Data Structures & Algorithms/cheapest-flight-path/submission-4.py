class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i: [] for i in range(n)}
        for u, v, price in flights:
            adj[u].append((v, price))

        pq = [(0, src, 0)]
        min_stops = [float('inf')] * n

        while pq:
            cost, node, stops = heapq.heappop(pq)
            
            if node == dst:
                return cost 

            if stops > k:
                continue
            
            if min_stops[node] <= stops:
                continue
            
            min_stops[node] = stops
            for v, price in adj[node]:
                heapq.heappush(pq, (cost + price, v, stops + 1))

        return -1





        