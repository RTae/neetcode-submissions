# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Apply DFS to check a legth
        res = 0
        def dfs(node):
            nonlocal res

            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # check between which path is longer
            res = max(res, left+right)

            # and add this layer
            return 1 + max(left,right)
        
        dfs(root)
        return res