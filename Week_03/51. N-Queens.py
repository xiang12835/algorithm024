class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]

        回溯

        时间复杂度：O(N!)
        空间复杂度：O(N)
        """
        if n < 1:
            return []
        
        self.result = []

        # 之前的皇后的所攻击的位置（列、pie、na）
        self.cols = set()
        self.pie = set()
        self.na = set()
        
        self.backtrack(n, 0, [])
        
        return self.gen_result(n)
    
    def backtrack(self, n, row, cur_state):
        # recursion terminator
        if row >= n:
            self.result.append(cur_state)
            return
        
        # current level! Do it!
        for col in range(n):
            if col in self.cols or row + col in self.pie or row - col in self.na:
                # go die!
                continue
                
            # update flags
            self.cols.add(col)
            self.pie.add(row + col)
            self.na.add(row - col)
            
            self.backtrack(n, row + 1, cur_state + [col])
        
            # remove flags
            self.cols.remove(col)
            self.pie.remove(row + col)
            self.na.remove(row - col)
    
    def gen_result(self, n):
        board = []
        for res in self.result:
            for i in res:
                board.append('.' * i + 'Q' + '.' * (n-1-i))
        
        return [board[i:i+n]for i in range(0, len(board), n)]