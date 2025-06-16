class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # One solution could be a binary search on each row, but that seems
        # still a bit much.
        # Lets brute force this first.

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == target:
                    return True

        return False