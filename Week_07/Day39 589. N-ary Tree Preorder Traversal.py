"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]

        递归

        T: O(n)
        S: O(h)
        """
        res = []
        def dfs(root):
            if not root:
                return
            res.append(root.val)
            for child in root.children:
                dfs(child)
        
        dfs(root)
        return res