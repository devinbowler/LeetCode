class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqDict = Counter(nums)
        sortedNums = sorted(freqDict.items(), key=lambda x: x[1], reverse=True)
        return sortedNums[0][0]