class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        # I can just it go from top left to bottom right, the top right
        # to bottom left summing all elements, but to avoid the center one
        # twice I can either say distinctly at depth n // 2 skip.
        returnSum = 0
        n = len(mat)
        directions = [((0, 0), (1, 1)), ((0, n - 1), (1, -1))]

        for (x, y), (dx, dy) in directions:
            for idx in range(n):
                returnSum += mat[x][y]
                x += dx
                y += dy

        # I can subtract the middle value after summing these diagionals
        if n % 2 == 1:
            returnSum -= mat[n // 2][n // 2]

        return returnSum