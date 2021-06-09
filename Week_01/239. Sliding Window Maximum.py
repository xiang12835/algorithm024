class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        '''
        暴力法
        时间复杂度：O(n * k)
        '''

        if not nums:
            return []
        
        n = len(nums)
        r = []
        for i in range(n-k+1):
            windows = nums[i:i+k]
            r.append(max(windows))
        
        return r
        