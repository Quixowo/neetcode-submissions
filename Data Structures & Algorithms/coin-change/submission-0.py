class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [-1] * (amount + 1) #contains minimum coin amount to get to a certain amount
        
        def dfs(amount):
            if amount == 0:
                return 0
            elif amount < 0:
                return float('inf')
            
            if memo[amount] != -1:
                return memo[amount]
            
            currMin = float('inf')
            for coin in coins:
                res = 1 + dfs(amount - coin)
                currMin = min(currMin, res)
            
            memo[amount] = currMin
            return memo[amount]
        
        ans = dfs(amount)
        return ans if ans != float('inf') else -1
            