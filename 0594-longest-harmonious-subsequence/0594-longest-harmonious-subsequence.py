class Solution:
    def findLHS(self, nums: List[int]) -> int:
        # Okay so just find the longest sub array that difference is == 1.
        # I think maybe sorting this then doing a sliding window expanding and checking
        # our condition, then return window size once we get to the end.

        nums.sort()
        left, maxHarm = 0, 0
        for right in range(len(nums)):
            while nums[right] - nums[left] > 1:
                left += 1
            if nums[right] - nums[left] == 1:
                maxHarm = max(maxHarm, right - left + 1)
                
        return maxHarm