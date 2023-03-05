# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = Queue()
        queue.put(root)
        output = []
        curr = []
        level = 0
        while not queue.empty():
            size = queue.qsize()
            curr = []
            for i in range(size):
                temp = queue.get()
                if level % 2 == 0:
                    curr.append(temp.val)
                else:
                    curr.insert(0, temp.val)
                if temp.left:
                    queue.put(temp.left)
                if temp.right:
                    queue.put(temp.right)
            level = not level
            output.append(curr)
        return output
