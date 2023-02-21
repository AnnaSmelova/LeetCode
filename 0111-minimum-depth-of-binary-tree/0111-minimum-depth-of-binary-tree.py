# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def get_min_len(root):
            if root is None:
                return 0
            if root.left is None:
                return get_min_len(root.right) + 1
            if root.right is None:
                return get_min_len(root.left) + 1
            return min(get_min_len(root.left), get_min_len(root.right)) + 1
        return get_min_len(root)