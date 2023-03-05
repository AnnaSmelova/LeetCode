# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        if not root:
            return []
        def dfs(node):
            if not node.left and not node.right:
                stack.append(node.val)
            else:
                if node.left:
                    dfs(node.left)
                stack.append(node.val)
                if node.right:
                    dfs(node.right)
        dfs(root)
        return stack
    