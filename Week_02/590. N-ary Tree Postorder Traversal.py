"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        """
        递归

        T: O(N)
        S: O(h)
        """
        res = []
        def dfs(root):
            if not root:
                return
            for child in root.children:
                dfs(child)
            res.append(root.val)
        dfs(root)
        return res
    

    res = []
        def helper(root):
            if not root:
                return
            res.append(root.val)
            for child in root.children:
                helper(child)
        helper(root)
        return res

