class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int

        DP

        T: O(n)
        S: O(1)

        fn = f1 + f2

        思考：
        
        1个，2个，3个台阶（easy)

        相邻两步的步伐不能相同（medium）
        """

        if n < 3:
            return n
        
        f1 = 1
        f2 = 2
        for i in range(3, n+1): # 易错
            fn = f1 + f2
            f1 = f2
            f2 = fn
        
        return fn