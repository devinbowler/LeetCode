class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # One solution could be a binary search on each row, but that seems
        # still a bit much.
        # Lets brute force this first.
        # Okay we can just look top right or bottom left and based off the number there
        # eliminate a row or col.

        n, m = len(matrix), len(matrix[0])
        r, c = n - 1, 0

        while r >= 0 and c < m:
            curNum = matrix[r][c]
            if curNum == target:
                return True
            elif curNum < target:
                c += 1
            else:
                r -= 1
        return False