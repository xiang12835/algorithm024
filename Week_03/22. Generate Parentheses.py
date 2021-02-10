class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        left 已经使用了的左括号的个数
        right 已经使用了的右括号的个数

        T: O(2^n)
        """
        self.l = []
        self._recursion(0, 0, n, "")
        return self.l

    def _recursion(self, left, right, n, result):
        # terminator
        if left == n and right == n:
            self.l.append(result)

        # process current logic: left, right
        # drill down
        if left < n:
            self._recursion(left+1, right, n, result+"(")
        
        if right < n and right < left:
            self._recursion(left, right+1, n, result+")")

        # reverse states