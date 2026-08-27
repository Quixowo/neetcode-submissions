class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def dfs(i, curr_amount):
            if (i, curr_amount) in memo:
                return memo[(i, curr_amount)]
            if i >= len(coins) or curr_amount > amount:
                return 0
            if curr_amount == amount:
                return 1

            combinations = dfs(i, curr_amount + coins[i]) + dfs(i + 1, curr_amount)
            memo[(i, curr_amount)] = combinations
            
            return memo[(i, curr_amount)]
        
        return dfs(0, 0)