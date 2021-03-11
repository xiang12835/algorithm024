class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        dp[i] = max(dp[i-1] * a[i],a[i])

        T: O(n)
        S: O(n)
        """
        n = len(nums)
        maxdp = [nums[0]] * n
        mindp = [nums[0]] * n
        
        for i in xrange(1, n):
            maxdp[i] = max(nums[i], maxdp[i-1]*nums[i], mindp[i-1]*nums[i])
            mindp[i] = min(nums[i], maxdp[i-1]*nums[i], mindp[i-1]*nums[i])
            
        return max(maxdp)
        