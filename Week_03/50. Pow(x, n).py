class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        暴力法

        T：O(n)
        S：O(1)
        """
        if n < 0:
            n = -n
            x = 1 / x
            
        r = 1
        for i in range(n):
            r *= x
        
        return r


class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        分治法

        T：O(logn)，即为递归的层数。
        S：O(logn)，即为递归的层数。这是由于递归的函数调用会使用栈空间。

        """

        if n < 0:
            n = -n
            x = 1 / x
        
        return self._dc(x, n)

    def _dc(self, x, n):
        # terminator
        if n == 0:
            return 1.0

        # process (split your big problems)
        half = self._dc(x, n//2)

        # drill down (subproblems), merge (subresult)
        if n % 2 == 0:
            # even
            return half * half
        else:
            # odd
            return half * half * x
        
        # reverse states
        
        

