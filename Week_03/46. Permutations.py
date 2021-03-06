# coding=utf-8

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        回溯

        path 变量是一个栈

        对象类型变量在传参的过程中，复制的是变量的地址。这些地址被添加到 res 变量，但实际上指向的是同一块内存地址，因此我们会看到 6 个空的列表对象。解决的方法很简单，在 res.add(path); 这里做一次拷贝即可。

        布尔数组 used，初始化的时候都为 false 表示这些数还没有被选择，当我们选定一个数的时候，就将这个数组的相应位置设置为 true ，这样在考虑下一个位置的时候，就能够以 O(1)O(1) 的时间复杂度判断这个数是否被选择过，这是一种「以空间换时间」的思想。

        T: O(n×n!)
        S: O(n×n!)
        """
        size = len(nums)
        if len(nums) == 0:
            return []

        used = [False for _ in range(size)]
        res = []
        self.backtrack(nums, size, 0, [], used, res)
        return res
    
    def backtrack(self, nums, size, depth, path, used, res):
            if depth == size:
                res.append(path[:]) # 易错
                return

            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

                    self.backtrack(nums, size, depth + 1, path, used, res)

                    used[i] = False
                    path.pop()