class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount, curStreak = 0, 0
        for each in nums:
            print(curStreak)
            if each == 1:
                curStreak += 1
                maxCount = max(maxCount, curStreak)
            else:
                curStreak = 0

        return max(maxCount, curStreak)