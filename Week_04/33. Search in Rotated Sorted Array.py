class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        顺序查找
        T: O(n)
        S: O(1)
        """
        for num in nums:
            if num == target:
                return nums.index(target)
        
        return -1

        