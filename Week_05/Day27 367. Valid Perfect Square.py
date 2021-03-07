class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool

        二分查找

        T: O(logN)
        S: O(1)
        """

        l = 0
        r = num
        while l <= r:
            mid = l + (r - l) / 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                r = mid - 1
            else:
                l = mid + 1
        return False