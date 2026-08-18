class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        distances = {i: [] for i in range(len(points))}
        for i in range(len(points)):
            x1, y1 = points[i]

            for j in range(i + 1, len(points)):
                x2, y2 = points[j]

                manhattan = abs(x1 - x2) + abs(y1 - y2)

                distances[i].append((manhattan, j))
                distances[j].append((manhattan, i))
        
        res = 0
        visited = set()

        heap = [[0, 0]] #point_so_far, index
        while len(visited) < len(points):
            cost, index = heapq.heappop(heap)

            if index in visited:
                continue

            visited.add(index)
            res += cost

            for nei_cost, nei_index in distances[index]:
                if nei_index not in visited:
                    heapq.heappush(heap, [nei_cost, nei_index])

        return res
                





        