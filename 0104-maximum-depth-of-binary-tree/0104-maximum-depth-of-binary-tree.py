# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        level = 0
        if root == None:
            return level
        q = deque()
        q.append((root, 1))
        while q:
            cur_node, d = q.popleft()
            level = max(level, d)
            if cur_node.left:
                q.append((cur_node.left, d+1))
            if cur_node.right:
                q.append((cur_node.right, d+1))
        return level