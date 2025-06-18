class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sortedSet = sorted(set(nums), reverse=True)
        for each in sortedSet:
            if len(sortedSet) >= 3:
                return sortedSet[2]
            else:
                return sortedSet[0]