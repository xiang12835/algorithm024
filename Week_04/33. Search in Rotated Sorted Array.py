class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        顺序查找
        T: O(n)
        S: O(1)
        """
        for num in nums:
            if num == target:
                return nums.index(target)
        
        return -1


class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        """
        五遍刷题；四步做题

        法1. 暴力：还原-可以用二分查找去还原 O(logN) -> 升序 -> 二分：O(logN)
        法2. 二分查找：a) 单调 b) 边界 c) index
        """
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

