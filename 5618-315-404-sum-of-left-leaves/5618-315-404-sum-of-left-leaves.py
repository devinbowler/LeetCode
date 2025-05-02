# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, total):
            if not node:
                return total

            if node.left and not node.left.left and not node.left.right:
                total += node.left.val

            total = dfs(node.left, total)
            total = dfs(node.right, total)
            return total

        return dfs(root, 0)