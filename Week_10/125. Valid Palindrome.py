class Solution:
    def isPalindrome(self, s: str) -> bool:

        ss = ''.join(c for c in s.lower() if c.isalnum())
        return ss[::-1] == ss


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        双指针 - 左右夹逼

        T：O(|s|)，其中 |s| 是字符串 s 的长度。
        S：O(1)。
        """
        s = s.lower()
        n = len(s)
        l = 0
        r = n - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True


