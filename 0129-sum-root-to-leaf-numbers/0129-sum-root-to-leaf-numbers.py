# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum_ = 0
        self.utils(root, '')
        return self.sum_

    def utils(self, root, s):
        if not root:
            return
        
        s += str(root.val)
        if not root.left and not root.right:
            self.sum_ += int(s)
            return
        self.utils(root.left, s)
        self.utils(root.right, s)

