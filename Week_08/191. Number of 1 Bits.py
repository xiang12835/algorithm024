class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int

        1. for loop: 0 -- 32
        2. %2, /2
        3. &1, x = x >> 1; (32)
        4. x = x & (x - 1)
        """
        count = 0
        while n:
            count += 1
            n = n & (n - 1)
        return count
