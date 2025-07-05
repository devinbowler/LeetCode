class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        result = []
        alternate = True
        for row in range(len(grid)):
            if row % 2 == 0:
                for col in range(len(grid[0])):
                    if alternate:
                        result.append(grid[row][col])
                        alternate = False
                    else:
                        alternate = True
            else:
                for col in reversed(range(len(grid[0]))):
                    if alternate:
                        result.append(grid[row][col])
                        alternate = False
                    else:
                        alternate = True
            

        return result