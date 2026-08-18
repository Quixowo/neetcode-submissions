class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i: [] for i in range(n)}
        components_count = 0
        visited = set()
        for node, otherNode in edges:
            adjList[node].append(otherNode)
            adjList[otherNode].append(node)

        def dfs(node):
            visited.add(node)
            for nei in adjList[node]:
                if nei not in visited:
                    dfs(nei)


        for i in range(n):
            if i not in visited:
                dfs(i)
                components_count += 1
        
        return components_count
            
