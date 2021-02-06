class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        排序
        T: O(NlogN)
        S: O(logN)
        """
        return sorted(s) == sorted(t)

class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        哈希表：用字数统计，因为只可能是26个字母
        T：O(n)，其中 n 为 s 的长度。
        S：O(S)，其中 S 为字符集大小，此处 S=26。
        """
        if len(s) != len(t):
            return False

        charCount = [0] * 26
        for c in s:
            charCount[ord(c)-97] += 1
        
        for e in t:
            charCount[ord(e)-97] -= 1
            if charCount[ord(e)-97] < 0:
                return False
        
        return True
