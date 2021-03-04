class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]

        # 转成数字加一后再转换成列表输出
        T: O(n)
        S: O(1)
        """
        s = 0
        for digit in digits:
            s = s * 10 + digit
        
        s += 1
        return [int(c) for c in str(s)]