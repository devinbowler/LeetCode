class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freqNum = Counter(nums)
        result = []

        # I just want to do a freq counter then add all values of 2 to an array then return.
        for each in nums:
            if freqNum[each] == 2 and each not in result:
                result.append(each)

        return result