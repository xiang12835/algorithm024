class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        
        排序 + 左右夹逼
        
        T: O(n^3)
        S: O(log n)
        """
        n, res = len(nums), []
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:   # 因为i=0这个元素会直接往下执行
                continue
            if i+3 <= n-1:
                if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                    break
            if i < n-3:
                if nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target:
                    continue
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:   # 因为j=i+1这个元素会直接往下执行
                    continue
                l, r = j+1, n-1
                while l < r:
                    tmp = nums[i] + nums[j] + nums[l] + nums[r]
                    if tmp == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]: 
                            l += 1
                        while l < r and nums[r] == nums[r+1]: 
                            r -= 1
                    elif tmp > target:
                        r -= 1
                    else:
                        l += 1
        return res