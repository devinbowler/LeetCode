class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index1, num1 in enumerate(nums):
            num = target - num1
            if num in nums[index1 + 1:]:
                tempNums = nums[index1 + 1:]
                print(num, tempNums)
                return [index1, tempNums.index(num) + (index1 + 1)]