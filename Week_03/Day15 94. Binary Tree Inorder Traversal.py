class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        递归

        T: O(n)
        S: O(h)
        """

        r = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            r.append(root.val)
            dfs(root.right)
        dfs(root)

        return r
