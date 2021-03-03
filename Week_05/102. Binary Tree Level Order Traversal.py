# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

        队列

        cur_data 来记录当前层的数据
        cur_size 当前这一层的节点个数

        T：每个点进队出队各一次，故渐进时间复杂度为 O(n)。
        S：队列中元素的个数不超过 n 个，故渐进空间复杂度为 O(n)。
        """

        if not root:
            return []

        ans = []
        queue = [root]

        while queue:
            cur_data = []
            cur_size = len(queue)

            for _ in range(cur_size):
                node = queue.pop(0)
                cur_data.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            ans.append(cur_data)
        return ans
