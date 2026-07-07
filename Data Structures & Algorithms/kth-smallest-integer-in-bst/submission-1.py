# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        visits = []
        self.helper(root, visits)
        return visits[k-1]

    def helper(self, root: [TreeNode], visits: list):
        if root is not None:
            self.helper(root.left, visits)
            visits.append(root.val)
            self.helper(root.right, visits)