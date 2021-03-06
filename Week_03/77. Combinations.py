# coding=utf-8

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k <= 0 or n < k:
            return []
        
        res = []
        # 从 1 开始是题目的设定
        self.backtrack(n, k, 1, [], res);
        return res
    
    def backtrack(self, n, k, begin, path, res):
        # 递归终止条件是：path 的长度等于 k
        if len(path) == k:
            res.append(path[:])
            return

        # 遍历可能的搜索起点
        for i in range(begin, n+1):
            # 向路径变量里添加一个数
            path.append(i)
            # 下一轮搜索，设置的搜索起点要加 1，因为组合数理不允许出现重复的元素
            self.backtrack(n, k, i + 1, path, res)
            # 重点理解这里：深度优先遍历有回头的过程，因此递归之前做了什么，递归之后需要做相同操作的逆向操作
            path.pop()
