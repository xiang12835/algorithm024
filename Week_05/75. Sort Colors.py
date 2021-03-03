class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        双指针
        
        三路快速排序方法

        设置三个 l, r, i 定义：nums[0...l] == 0，nums[l+1...i-1] = 1，nums[r...n-1] == 2，遍历一遍改数列保持这个定义。

        T: O(N)
        S: O(1)
        """
        
        left = -1
        right = len(nums)
        i = 0
        while i < right:
            if nums[i] == 0:
                left += 1
                nums[left], nums[i] = nums[i], nums[left]
                i += 1
            elif nums[i] == 2:
                right -= 1
                nums[right], nums[i] = nums[i], nums[right]
            else:
                i += 1
