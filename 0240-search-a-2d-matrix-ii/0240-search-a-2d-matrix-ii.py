class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # One solution could be a binary search on each row, but that seems
        # still a bit much.
        # Lets brute force this first.
        # What if we check the diagonal for greater or less than, if great we can eleminate
        # that row and column behind it but if less than we check the row and col behind it.
        m, n = len(matrix), len(matrix[0])
        def checkCorner(x, y):
            # Check x
            for idx in range(n):
                print(matrix[y][idx])
                if matrix[y][idx] == target:
                    return True
            # Check y
            for idx in range(m):
                if matrix[idx][x] == target:
                    return True
            return False

        for coord in range(min(m, n)):
            curNum = matrix[coord][coord]
            if curNum == target:
                return True
            else:
                if checkCorner(coord, coord):
                    return True

        return False