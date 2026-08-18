class Solution:
    def climbStairs(self, n: int, cache: dict = None) -> int:
        if cache is None:
            cache = {}
            
        if n == 1 or n == 0:
            return 1
            
        if n in cache:
            return cache[n]
            
        cache[n] = self.climbStairs(n - 1, cache) + self.climbStairs(n - 2, cache)
        return cache[n]