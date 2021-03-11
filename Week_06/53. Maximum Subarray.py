class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        最大子序和 = 当前元素自身最大 or 加上之前后最大
        dp[i] = max(nums[i], nums[i] + dp[i-1])

        T: O(n)
        S: O(n)
        """
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
        
        dp = nums
        for i in xrange(1,n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        
        return max(dp)