class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        distances = {i: float('inf') for i in range(1, n + 1)}
        distances[k] = 0
        minHeap = [(0, k)]

        while minHeap:
            curr_dist, curr_vertex = heapq.heappop(minHeap)

            if curr_dist > distances[curr_vertex]:
                continue

            for v, w in adj[curr_vertex]:
                time = curr_dist + w
                if time < distances[v]:
                    distances[v] = time
                    heapq.heappush(minHeap, (time, v))

        max_time = max(distances.values())
        return max_time if max_time < float('inf') else -1
