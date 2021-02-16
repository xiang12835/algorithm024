# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        队列

        cur_level来记录当前层的数据
        cur_size 当前这一层的节点个数

        T：每个点进队出队各一次，故渐进时间复杂度为 O(n)。
        S：队列中元素的个数不超过 n 个，故渐进空间复杂度为 O(n)。
        """
        if not root:
            return []
        
        res = []
        queue = [root]
        while queue:
            cur_size = len(queue)
            cur_level = []
            for _ in range(cur_size):
                node = queue.pop(0) # 易错
                cur_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(cur_level)
        
        return res
        