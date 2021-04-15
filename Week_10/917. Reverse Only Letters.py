class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str

        左右指针

        T: O(n)
        S: O(1)
        """
        letters = list(S)
        l = 0
        r = len(S) - 1
        while l < r:
            while l<r and not letters[l].isalpha():
                l += 1
            while l<r and not letters[r].isalpha():
                r -= 1
            letters[l], letters[r] = letters[r], letters[l]
            l += 1
            r -= 1
        return ''.join(letters)