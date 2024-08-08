class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def increasingBST(self, root):
        answer = []
        def dfs(node):
            if node:
                dfs(node.left)
                answer.append(node.val)
                dfs(node.right)
        dfs(root)
        new_tree = TreeNode(answer[0])
        current = new_tree
        for i in range(1, len(answer)):
            current.right = TreeNode(answer[i])
            current = current.right
        return new_tree
