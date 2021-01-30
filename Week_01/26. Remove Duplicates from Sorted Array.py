class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        快慢指针
        T: O(n)
        S: O(1)
        """
        j = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        
        return j + 1