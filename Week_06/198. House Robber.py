class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        DP

        法二：
        dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        T: O(N)
        S: O(N)
        """

        if not nums:
            return 0
        
        n = len(nums)

        if n == 1:
            return nums[0]
        
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        return dp[n-1]


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        T: O(N)
        S: O(1)
        """
        pre, cur = 0, 0
        for num in nums:
            pre, cur = cur, max(pre+num, cur)
        return cur
        