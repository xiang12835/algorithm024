class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        dp 自顶向下

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


class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        dp 自底向上

        T: O(mn)
        S: O(mn)
        """
        # 从 (i, j) 走到 <end> 的不同路径数
        dp = [[0] * n for _ in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m - 1 or j == n - 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
        return dp[0][0]
