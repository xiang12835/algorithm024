class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool

        贪心

        记录5和10的个数，如果有一个透支了，就说明不能满足找零

        T: O(n)
        S: O(1)
        """

        i = 0
        j = 0
        for bill in bills:
            if bill == 5:
                i += 1
            elif bill == 10:
                j += 1
                i -= 1
            else:
                if j == 0:
                    i -= 3
                else:
                    j -= 1
                    i -= 1
            
            if i < 0 or j < 0:
                return False
        return True