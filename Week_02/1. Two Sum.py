class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        哈希表
        T: O(n)
        S: O(n)
        """
        d = {}
        for i, v in enumerate(nums):
            if target - v in d:
                return [d[target - v], i]
            else:
                d[v] = i