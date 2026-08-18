class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        path = set()
        for prereq in prerequisites:
            preMap[prereq[0]].append(prereq[1])

        def dfs(node):
            if node in path:
                return False
            if preMap[node] == []:
                return True
        
            path.add(node)

            for nei in preMap[node]:
                if not dfs(nei):
                    return False

            path.remove(node)
            preMap[node] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True
            
