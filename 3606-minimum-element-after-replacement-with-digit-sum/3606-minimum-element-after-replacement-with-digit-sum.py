class Solution:
    def minElement(self, nums: List[int]) -> int:
        # oooo I think I have a good idea, if I treat each number as a string
        # I can loop through and add them as seprate ints, then just re-store
        # and return the min()

        for idx, each in enumerate(nums):
            tempSum = 0
            for char in str(each):
                tempSum += int(char)
            nums[idx] = tempSum

        return min(nums)