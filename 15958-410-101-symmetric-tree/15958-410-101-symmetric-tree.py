# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, level, build):
            if node is None:
                if level not in build:
                    build[level] = [1]
                else:
                    build[level].append(1)
                return build
            
            if level not in build:
                build[level] = [int(node.val)]
            else:
                build[level].append(int(node.val))

            dfs(node.left, level + 1, build)
            return dfs(node.right, level + 1, build)

        leftPath = dfs(root.left, 1, {})
        rightPath = dfs(root.right, 1, {})

        print(leftPath, rightPath)

        for level in leftPath:
            if level not in rightPath:
                return False
            if leftPath[level] != rightPath[level][::-1]:
                return False

        return True
            
