class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]

        left 已经使用了的左括号的个数
        right 已经使用了的右括号的个数

        T: O(2^n)
        """
        self.ans = []
        self.dfs(0, 0, n, '')
        return self.ans

    def dfs(self, l, r, n, s):
        if l == n and r == n:
            self.ans.append(s)
            return
        
        if l < n:
            self.dfs(l+1, r, n, s+"(") 
        if r < n and r < l:
            self.dfs(l, r+1, n, s+")")