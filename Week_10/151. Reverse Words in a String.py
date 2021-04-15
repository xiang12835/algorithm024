class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()

        words = s[::-1].split(' ')
        r = []
        for word in words:
            if word:
                r.append(word[::-1])
        
        return ' '.join(r)