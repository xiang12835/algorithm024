class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        迭代法
        """
        results = [[]]

        for num in nums:
            l = []
            for result in results:
                l.append(result+[num])

            results.extend(l)
        return results
