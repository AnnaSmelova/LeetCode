# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        return self.isSymmetricUtils(root.left, root.right)

    def isSymmetricUtils(self, left, right):
        if left == None and right == None:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        else:
            if not self.isSymmetricUtils(left.left, right.right):
                return False
            if not self.isSymmetricUtils(left.right, right.left):
                return False
            return True
            