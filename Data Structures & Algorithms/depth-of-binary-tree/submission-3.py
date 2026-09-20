# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Apply DFS

        if root is None:
            return 0
        
        # count this layer and compare which left or right node give more depth
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))