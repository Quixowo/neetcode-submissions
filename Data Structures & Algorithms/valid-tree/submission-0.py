class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(n)}
        visited = set()
        for node, otherNode in edges:
            adjList[node].append(otherNode)
            adjList[otherNode].append(node)

        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)
            for neighbor in adjList[node]:
                if neighbor == prev:
                    continue
                if not dfs(neighbor, node):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n