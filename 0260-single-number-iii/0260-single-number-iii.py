class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Not sure how good this runs but I could just do a frequency counter
        # then just filter through each value and if the value is 1 add it
        # to the return array.

        freqNums = Counter(nums)
        returnArr = []

        for num in nums:
            if freqNums[num] == 1:
                returnArr.append(num)
        
        return returnArr