class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        # 转成数字加一后再转换成列表输出
        T: O(n)
        S: O(1)
        """
        n = len(digits)
        countZero = 0
        for i in range(n):
            if digits[i] != 0:
                break
            countZero += 1

        s = 0
        for digit in digits:
            s = s * 10 + digit
        
        s += 1

        return [0] * (countZero-1) + [int(c) for c in str(s)]
