class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount <= 0:
            return 0
        
        if min(coins) > amount:
            return -1

        INT_MAX = 1<<32
        dp = [INT_MAX] * (amount +1)
        
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min((dp[i-coin] + 1), dp[i])
                    
        return dp[amount] if dp[amount] != INT_MAX else -1