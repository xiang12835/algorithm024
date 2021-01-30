class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        快慢指针
        T: O(n)
        S: O(1)
        """
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1