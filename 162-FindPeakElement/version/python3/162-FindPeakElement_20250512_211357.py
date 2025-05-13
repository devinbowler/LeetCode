# Last updated: 5/12/2025, 9:13:57 PM
# This was much easier then a medium to be honest, just a simple tracker of max value, if max value updates, change the new return index. Thought there would be time limit restraint here.
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        index = 0
        maxVal = nums[0]
        for idx, each in enumerate(nums):
            if each > maxVal:
                maxVal = each
                index = idx
        
        return index