class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        dfs

        T：O(MN)，其中 M 和 N 分别为行数和列数。
        S：O(MN)，在最坏情况下，整个网格均为陆地，深度优先搜索的深度达到 M*N。
        """
        # 检查参数
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])

        # 两层循环扫描，当发现是陆地时，将其周围相邻的岛屿都夷为平地
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j, m, n)
        return count

    def dfs(self, grid, i, j, m, n):
        if i < 0 or j < 0 or i >= m or j>= n or grid[i][j] != '1':
            return
        grid[i][j] = '0'
        self.dfs(grid, i + 1, j, m, n)
        self.dfs(grid, i - 1, j, m, n)
        self.dfs(grid, i, j + 1, m, n)
        self.dfs(grid, i, j - 1, m, n)