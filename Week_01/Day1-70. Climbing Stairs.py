class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int

        DP

        T: O(n)
        S: O(1)
        """

        if n < 3:
            return n

        f1 = 1
        f2 = 2

        for _ in range(3, n+1): # 易错
            fn = f1 + f2
            f1 = f2
            f2 = fn
        
        return fn