# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        seen = []
        def dfs(node):
            nonlocal seen
            if node is None:
                return

            seen.append(node.val)

            dfs(node.left)
            dfs(node.right)

        
        dfs(root)
        return len(seen)
            
