class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s: 
            return 0

        sign = -1 if s[0] == '-' else 1

        if s[0] in ['+', '-']:
            s = s[1:]

        r = 0
        for c in s:
            if c.isdigit():
                r = r * 10 + ord(c) - ord('0')
            else:
                break
        
        r = sign * r

        return max(-2 ** 31, min(r, 2**31 - 1))