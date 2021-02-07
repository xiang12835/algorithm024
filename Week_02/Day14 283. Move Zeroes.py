class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        快慢指针

        T: O(n)
        S: O(1)
        """
        n = len(nums)
        fast, slow = 0, 0
        while fast < n:
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        while slow < n:
            nums[slow] = 0
            slow += 1
            