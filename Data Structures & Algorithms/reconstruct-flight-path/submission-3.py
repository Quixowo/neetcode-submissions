class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res = ['JFK']
        adj = {src: [] for src, dst in tickets}
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)

        def dfs(ticket):
            if len(res) == len(tickets) + 1:
                return True
            if ticket not in adj: return False

            temp = list(adj[ticket])
            for i, v in enumerate(temp):
                adj[ticket].pop(i)
                res.append(v)

                if dfs(v): return True

                adj[ticket].insert(i, v)
                res.pop()
            
            return False
        
        dfs('JFK')

        return res
                
                