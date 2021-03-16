class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return []
        self.count = 0
        self.dfs(n, 0, 0, 0, 0)
        return self.count
    
    def dfs(self, n, row, col, pie, na):
        # 递归终止条件
        if row >= n:
            self.count += 1
            return
        
        bits = (~(col | pie | na)) & ((1 << n) - 1)  # 得到当前所有的空位，‘1’的位置就是能填皇后的位置
        
        while bits:
            p = bits & -bits  # 取到最低位的1
            bits = bits & (bits - 1)  # 去掉最低位的1，表示p位置上放入皇后
            self.dfs(n, row + 1, col | p, (pie | p) << 1, (na | p) >> 1)
            # 不需要 revert col, pie, na 的状态
            