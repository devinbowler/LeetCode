class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curSum = sum(nums[:k])
        maxSum = curSum

        for index in range(k, len(nums)):
            curSum += nums[index] - nums[index - k]
            maxSum = max(maxSum, curSum)

        return maxSum / k