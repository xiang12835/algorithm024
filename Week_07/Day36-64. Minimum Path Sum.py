class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        创建二维数组 dp，与原始网格的大小相同，dp[i][j] 表示从左上角出发到 (i,j) 位置的最小路径和。显然，dp[0][0]=grid[0][0]。对于 dp 中的其余元素，通过以下状态转移方程计算元素值。

        当 i>0 且 j=0 时，dp[i][0]=dp[i−1][0]+grid[i][0]

        当 i=0 且 j>0 时，dp[0][j]=dp[0][j−1]+grid[0][j]

        当 i>0 且 j>0 时，dp[i][j]=min(dp[i−1][j],dp[i][j−1])+grid[i][j]

        最后得到 dp[m−1][n−1] 的值即为从网格左上角到网格右下角的最小路径和

        T: O(mn)
        S: O(mn)
        """
        if not grid or not grid[0]:
            return 0
        
        row = len(grid)
        column = len(grid[0])

        dp = [[0] * column for _ in range(row)]
        dp[0][0] = grid[0][0]

        # 第一列, j = 0
        for i in range(1, row): 
            dp[i][0] = dp[i-1][0] + grid[i][0]

        # 第一行, i = 0
        for j in range(1, column): 
            dp[0][j] = dp[0][j-1] + grid[0][j]

        # 其他
        for i in range(1, row):
            for j in range(1, column):
                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]

        return dp[-1][-1]
