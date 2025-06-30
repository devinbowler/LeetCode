class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        # I mean I could have a running number that whatever would make the curSum
        # equal to 1 if negitive set that as the return value.

        startValue = 1
        runningSum = 0

        for each in nums:
            runningSum += each
            if runningSum < 1:
                while (runningSum + startValue) < 1:
                    startValue += 1
            
        return startValue