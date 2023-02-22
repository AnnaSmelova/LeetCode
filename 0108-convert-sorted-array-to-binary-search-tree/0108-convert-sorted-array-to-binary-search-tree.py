# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    @staticmethod
    def fix(root: TreeNode):
        left_height = 0 if root.left is None else root.left.height
        right_height = 0 if root.right is None else root.right.height
        root.height = max(left_height, right_height) + 1
        root.balance = left_height - right_height
        return

    def small_rotate(self, p, dir='left'):
        if dir == 'left':
            q = p.right
            p.right = q.left
            q.left = p
        else:
            q = p.left
            p.left = q.right
            q.right = p
        self.fix(p)
        self.fix(q)
        return q

    def big_rotate(self, p, dir='left'):
        if dir == 'left':
            p.right = self.small_rotate(p.right, 'right')
        else:
            p.left = self.small_rotate(p.left, 'left')
        return self.small_rotate(p, dir)

    def balance(self, root):
        if root is None:
            return None
        if root.balance == -2 and root.right.balance <= 0:
            root = self.small_rotate(root, 'left')
        elif root.balance == -2 and root.right.balance > 0:
            root = self.big_rotate(root, 'left')
        elif root.balance == 2 and root.left.balance >= 0:
            root = self.small_rotate(root, 'right')
        elif root.balance == 2 and root.left.balance < 0:
            root = self.big_rotate(root, 'right')
        return root

    @staticmethod
    def get_height(root):
        if root is None:
            return 0
        return root.height

    def get_balance(self, root):
        if root is None:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def insert_node(self, root, value):
        if root is None:
            node = TreeNode(value)
            node.height = 1
            node.balance = 0
            return node
        if root.val > value:
            root.left = self.insert_node(root.left, value)
        elif root.val < value:
            root.right = self.insert_node(root.right, value)
        self.fix(root)
        return self.balance(root)

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        root = TreeNode(val=nums[n//2])
        for value in nums:
            if value != nums[n//2]:
                root = self.insert_node(root, value)
        return root

        