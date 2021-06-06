class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        for i in range(n):
            if s.index(s[i]) != t.index(t[i]):
                return False
        
        return True
        