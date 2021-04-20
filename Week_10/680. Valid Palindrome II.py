class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        双指针+递归
        """
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return self.isPalindrome(s, l, r-1) or self.isPalindrome(s, l+1, r)
        return True
        
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True