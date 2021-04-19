class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        lenP = len(p)
        lenS = len(s)
        p = "".join(sorted(p))
        r = []
        for i in range(lenS - lenP + 1):
            if "".join(sorted(s[i:i+lenP])) == p:
                r.append(i)
        
        return r
