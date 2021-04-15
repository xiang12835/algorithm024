class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        """
        我们直接翻转每个 2k 字符块。

        T: O(n)
        S: O(n)
        """
        l = list(s)
        n = len(l)
        for i in range(0, n, 2*k):
            l[i:i+k] = reversed(l[i:i+k])
        return ''.join(l)