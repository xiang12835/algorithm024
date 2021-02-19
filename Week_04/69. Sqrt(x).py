class Solution:
    def mySqrt(self, x: int) -> int:
        """
        二分查找
        y = x ^ 2, (x>0): 抛物线，在y轴右侧，单调递增；上下界

        T: O(x)
        S: O(1)
        """
        if x == 0:
            return 0
            
        l = 1
        r = x
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                r = mid - 1
            else:
                l = mid + 1
        return r # 当无整数平方根时，取小值
        
        