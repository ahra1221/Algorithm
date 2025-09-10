# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = deque([(root.left, root.right)])
        while q:
            a,b = q.popleft()
            if not a and not b:
                continue
            if not a or not b or a.val != b.val:
                return False
            q.append((a.left, b.right))
            q.append((b.left, a.right))
        return True