# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(node, path):
            if not node:
                path.append("None")
                return path

            path.append(node.val)

            dfs(node.left, path)
            dfs(node.right, path)
            return path

        resOne = dfs(p, [])
        resTwo = dfs(q, [])

        if resOne == resTwo:
            return True
        else:
            return False