class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # I can actually just sort then if there is ever a number equal to its neighbor
        # add it to the return array.

        returnArr = []
        nums.sort()
        for idx in range(len(nums) - 1):
            if nums[idx] == nums[idx + 1]:
                returnArr.append(nums[idx])

        return returnArr