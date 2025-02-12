# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depthVal = 0
        def dfs(node, depth):
            nonlocal depthVal
            if not node:
                return
            depthVal = max(depthVal, depth + 1)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, depthVal)
        return depthVal