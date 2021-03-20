class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]

        DFS + 剪枝

        left 已经使用了的左括号的个数
        right 已经使用了的右括号的个数

        T: O(2^n)
        """
        self.l = []
        self.dfs(0, 0, n, "")
        return self.l

    def dfs(self, l, r, n, path):
        # terminator
        if l == n and r == n:
            self.l.append(path)

        # current

        # drill
        if l < n:
            self.dfs(l+1, r, n, path+"(")
        if r < n and r < l:
            self.dfs(l, r+1, n, path+")")

        # reverse
