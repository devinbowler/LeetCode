class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        arrSum = sum(nums)
        seen, have = 0, arrSum

        for index, each in enumerate(nums):
            have -= each
            if seen == have:
                return index
            seen += each

        return -1