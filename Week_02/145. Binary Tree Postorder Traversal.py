# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.r = []
        self.dfs(root)
        return self.r

    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        self.dfs(root.right)
        self.r.append(root.val)