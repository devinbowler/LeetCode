class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        # Any cell '1' with < 2 neighboring '1's goes to 0.
        # Any cell '1' with 2 or 3 neighboring '1's stays a 1.
        # Any cell '1' with > 3 neighboring '1's goes to 0.
        # Any cell '0' with 3 '1' neighbors goes to '1'.

        # There is probably some way to make this faster than O(nxm) but I am going to cell by cell.
        # And the some because each cell needs all neighbors checked.

        rows, cols = len(board), len(board[0])
        directions = [(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)]

        def checkNeighbors(x, y):
            # Check each direction for a 1 or 0, increment a count, then decide what the cell
            # changes to after the count is made.
            count = 0
            for dx, dy in directions:
                nx, ny = (dx + x), (dy + y)
                if 0 <= nx < rows and 0 <= ny < cols:
                    count += board[nx][ny]
            return count

        # I know we want in place but I am not dealing with that, so ill make a copy for now

        new_board = [[0] * cols for each in range(rows)]

        for row in range(rows):
            for col in range(cols):
                neighborCount = checkNeighbors(row, col)

                # This should work since we set an all 0 copy, so we only want to set the ones.
                if board[row][col] == 1:
                    if neighborCount == 2 or neighborCount == 3:
                        new_board[row][col] = 1
                else:
                    if neighborCount == 3:
                        new_board[row][col] = 1

        # Now make the orignal the copy
        for r in range(rows):
            for c in range(cols):
                board[r][c] = new_board[r][c]
        