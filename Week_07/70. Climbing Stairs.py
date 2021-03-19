class Solution1:
    def climbStairs(self, n: int) -> int:
        """
        递归

        f(1) = 1
        f(2) = 2
        f(n) = f(n-1) + f(n-2)

        T: O(2^n)
        """
        if n < 3:
            return n

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


class Solution2:
    def climbStairs(self, n: int) -> int:
        """
        法二：递归 + 记忆化
        T: O(n)
        """
        if n < 3:
            return n
        d = {}
        if n not in d:
            d[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return d[n]


class Solution3(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int

        DP

        dp[n] = dp[n-1] + dp[n-2]

        dp[1] = 1
        dp[2] = 2


        T: O(n)
        S: O(n)

        if n == 1:
            return 1

        if n == 2:
            return 2

        l = [1, 2]
        for _ in xrange(3, n + 1):
            l.append(l[-2] + l[-1])

        return l[-1]


        法三：DP

        自下而上

        dp[n] = dp[n-1] + dp[n-2]

        T: O(n)
        S: O(n)
        """
        if n < 3:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


class Solution4(object):
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

        f1 = 1
        f2 = 2
        fn = 0
        for _ in range(3, n + 1):  # 易错
            fn = f1 + f2
            f1 = f2
            f2 = fn

        return fn
