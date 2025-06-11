class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # I want a function that on loop can be called with a new 'rotated' array.
        # It will return a sum, then either update or keep a max value.
        # It's taking so long I am computing the same thing multiple times if you
        # think about it, on 1 thing is really chaning so I need to utilize that.
        returnVal = float('-inf')
        n = len(nums)
        totalSum = sum(nums)
        currentValue = sum(idx * num for idx, num in enumerate(nums))

        returnVal = currentValue
        for iteration in range(1, n):
            currentValue += totalSum - (n * nums[-iteration])
            returnVal = max(returnVal, currentValue)
        
        return returnVal