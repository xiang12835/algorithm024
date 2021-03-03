class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        排序算法；左右碰撞

        T：O(N^2)，其中 N 是数组 nums 的长度。

        S：O(logN)。
        """
        nums.sort()
        
        ans = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i + 1
            r = n - 1
            
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        return ans
