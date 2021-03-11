class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        DP

        a. subproblems
        b. dp array : f(n) 表示凑到面值为n, 最少硬币个数
        c. dp equation : f(n) = min{f(n-k), for k in [1,2,5]} + 1
        
        T：O(N*amount) = O(N)
        S：O(amount)
        """
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x-coin] + 1)

        return dp[amount] if dp[amount] != float("inf") else -1