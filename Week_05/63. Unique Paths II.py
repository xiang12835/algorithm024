class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        dp 自顶向下

        T: O(mn)
        S: O(mn)
        """
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        if n == 0:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0

        # 初始化第一行和第一列的二维数组
        dp = [[0] * n for i in range(m)]
        dp[0][0] = 1
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:  # 第一行无障碍
                dp[0][j] = dp[0][j-1]
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:  # 第一列无障碍
                dp[i][0] = dp[i-1][0]

        # 计算其他行列的二维数组
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:  # 障碍物
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]
