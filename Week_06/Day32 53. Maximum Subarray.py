class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """

        DP 

        ms(i) = max(ms[i-1]+ a[i],a[i])

        T: O(N)
        S: O(N)
        """

        if not nums:
            return 0

        n = len(nums)

        if n == 0:
            return nums[0]
        
        dp = [nums[0]] * n

        for i in range(1, n):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        
        return max(dp)