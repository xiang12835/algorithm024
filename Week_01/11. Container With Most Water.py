class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        双指针 - 左右碰撞
        """
        l = 0
        r = len(height) - 1
        ans = 0
        while l <= r:
            area = (r - l) * min(height[l],height[r])
            ans = max(ans, area)
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                l += 1
                r -= 1

        return ans