class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        纵向扫描

        T：O(mn)，其中 m 是字符串数组中的字符串的平均长度，n 是字符串的数量。最坏情况下，字符串数组中的每个字符串的每个字符都会被比较一次。

        S：O(1)。使用的额外空间复杂度为常数。
        """
        prefix = ""
        for item in zip(*strs):
            bag = set(item)
            if len(bag) == 1:
                prefix += bag.pop()
            else:
                break
        return prefix
