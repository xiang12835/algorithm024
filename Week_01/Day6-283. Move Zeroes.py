class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead

        法一：快慢指针

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

class Solution1(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        # 法二：快排思想
        # T: O(n)
        # S: O(1)
        """
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != 0: # 当前元素!=0，就把其交换到左边，等于0的交换到右边
                nums[i], nums[j] = nums[j], nums[i]
                j += 1