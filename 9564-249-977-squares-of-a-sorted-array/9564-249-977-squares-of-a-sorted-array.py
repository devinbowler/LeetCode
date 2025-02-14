class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        newArray = []
        for each in nums:
            squareRes = each * each
            newArray.append(squareRes)

        newArray.sort()
        return newArray