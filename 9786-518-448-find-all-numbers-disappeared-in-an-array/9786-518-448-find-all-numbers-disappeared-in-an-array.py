class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
            num = abs(nums[i])
            index = num - 1

            if nums[index] > 0:
                nums[index] = -nums[index]

        result = []
        for i in range(n):
            if nums[i] > 0:
                result.append(i + 1)

        return result
        