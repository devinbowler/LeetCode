class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        # Okay I can probably just count all the 1's in each row and col.
        # Then loop through the entire matrix and anytime I find a 1, check to see if
        # there is a 1 in the row and col, then increase a count to return.
        rows, cols = len(grid), len(grid[0])

        row_count = [sum(row) for row in grid]
        col_count = [sum(grid[r][c] for r in range(rows)) for c in range(cols)]

        # Now I can just loop through the matrix ideally and add to a total for each 1 on the
        # col and row.
        total = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    total += (row_count[i] - 1)  * (col_count[j] - 1)

        return total