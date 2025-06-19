class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount, curStreak = 0, 0
        streak = False
        for each in nums:
            print(curStreak)
            if each == 1:
                if streak == True:
                    curStreak += 1
                    maxCount = max(maxCount, curStreak)
                else:
                    streak = True
                    curStreak = 1
            else:
                streak = False

        return max(maxCount, curStreak)