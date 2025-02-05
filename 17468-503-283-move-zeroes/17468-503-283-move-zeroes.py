class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index, moves = 0, 0
        while index < len(nums) - 1 and moves != len(nums) - 1:
            if nums[index] == 0:
                del nums[index]
                nums.append(0)
            else:
                index += 1
            moves += 1
