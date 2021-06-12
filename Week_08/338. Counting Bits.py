class Solution:
    def countBits(self, n: int) -> List[int]:

        """
        时间复杂度：O(nlogn)
        空间复杂度：O(1)
        """

        def hammingWeight(n):
            count = 0
            while n:
                count += 1
                n = n & (n - 1)
            return count

        res = []
        for i in range(n + 1):
            res.append(hammingWeight(i))
        return res


class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        1. subproblem

        2. dp array
        令 y=x & (x−1)，则 y 为将 x 的最低设置位从 1 变成 0 之后的数，显然 0≤y<x，bits[x]=bits[y]+1。因此对任意正整数 x，都有 bits[x]=bits[x & (x−1)]+1。
        
        3. dp equation

        T: O(n)
        S: O(1)
        """

        bits = [0]
        for x in range(1, n+1):
            bits.append(bits[x&(x-1)] + 1)
        
        return bits

