class Solution:
    def reverseWords(self, s: str) -> str:
        r = []
        for word in s.split(' '):
            r.append(word[::-1])
        
        return ' '.join(r)
