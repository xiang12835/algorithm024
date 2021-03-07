class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        size = len(nums)
        if size == 0:
            return []
        
        used = [False for _ in range(size)]
        res = []
        self.backtrace(nums, size, 0, [], used, res)
        return res
    
    def backtrace(self, nums, size, depth, path, used, res):
        if depth == size:
            res.append(path[:])
            return
        
        for i in range(size):
            if not used[i]:
                used[i] = True
                path.append(nums[i])
                self.backtrace(nums, size, depth + 1, path, used, res)

                used[i] = False
                path.pop()