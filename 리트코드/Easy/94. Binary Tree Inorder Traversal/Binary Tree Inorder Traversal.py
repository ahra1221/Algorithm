class Solution(object):
    def inorderTraversal(self, root):
        answer = []
        
        def dfs(node):
            if node:
                dfs(node.left)
                answer.append(node.val)
                dfs(node.right)
                
        dfs(root)
        return answer
