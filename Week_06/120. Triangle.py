class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        brute-force, 递归，n层：left or right: 2^n

        优化：记忆化搜索

        DP:
        a. 重复性（分治）：problem(i,j) = min(sub(i+1, j), sub(i+1,j+1)) + a(i,j)
        b. 定义状态数组: f[i,j]
        c. DP 方程: f[i,j] = min(f[i+1,j], f[i+1,j+1]) + a[i,j]

        由底向上
        """
        dp = triangle
        for i in range(len(dp)-2, -1, -1):
            for j in range(len(dp[i])):
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + dp[i][j]
        
        return dp[0][0]
