class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        gridMap = {}
        for row in grid:
            rowTup = tuple(row)
            if rowTup in gridMap:
                gridMap[rowTup][0] += 1
            else:
                gridMap[rowTup] = [1]

        for col in zip(*grid):
            colTup = tuple(col)
            if colTup in gridMap:
                gridMap[colTup].append(gridMap[colTup][0])
        
        gridVals = list(gridMap.values())
        
        returnSum = 0
        for each in gridVals:
            if len(each) > 1:
                for index in range(1, len(each)):
                    returnSum += each[index]

        return returnSum