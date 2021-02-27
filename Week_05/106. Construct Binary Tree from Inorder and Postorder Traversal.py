# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        递归

        T: O(n), n 是树中的节点个数
        S: O(n), 递归借助了额外的栈空间来完成，栈的深度为n
        """
        if not inorder: # 实际上inorder 和 postorder一定是同时为空的，因此你无论判断哪个都行
            return
        root = TreeNode(postorder[-1])
        i = inorder.index(root.val)
        root.left = self.buildTree(inorder[:i], postorder[:i])
        root.right = self.buildTree(inorder[i+1:], postorder[i:-1])
        return root
