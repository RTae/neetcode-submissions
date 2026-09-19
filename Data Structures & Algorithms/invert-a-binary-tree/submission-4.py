# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # The goal is to swap a node like a mirror
        # we can using DFS to swap by layer

        # check if node is not None first
        if root is None: return None

        # swap
        root.left, root.right = root.right, root.left

        # go deeper
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root