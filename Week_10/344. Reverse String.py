class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.

        双指针 - 左右夹逼
        T：O(N)，其中 N 为字符数组的长度。一共执行了 N/2 次的交换。
        S：O(1)。只使用了常数空间来存放若干变量。
        """
        l = 0
        r = len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

class Solution1(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """

        return s[::-1]

class Solution2(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """

        def recursion(left, right):
            """
            T：O(N)，执行了 N/2 次的交换。
            S：O(N)，递归过程中使用的堆栈空间。
            """
            if left >= right:
                return
            s[left], s[right] = s[right], s[left]
            recursion(left + 1, right - 1)

        recursion(0, len(s) - 1)
