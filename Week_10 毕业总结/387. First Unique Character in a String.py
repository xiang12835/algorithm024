class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        字典
        
        T: O(N)
        S: O(N)
        """
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1

        for i, c in enumerate(s):
            if d[c] == 1:
                return i
        
        return -1
