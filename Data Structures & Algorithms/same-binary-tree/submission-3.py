# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # the idea is apply DFS and check two node by layer

        # mean it's None
        if not p and not q:
            return True
        
        # mean value are eqaul, and then we check deeper
        # check left and right are equal or not 
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # if not return False
        else:
            return False