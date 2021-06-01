class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        dp 

        T: O(mn)
        S: O(mn)
        """
        # 从 <start> 走到 (i, j) 的不同路径
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]