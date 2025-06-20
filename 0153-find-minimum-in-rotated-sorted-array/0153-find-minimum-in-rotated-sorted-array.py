class Solution:
    def findMin(self, nums: List[int]) -> int:
        # actually this may still be just a binary search even though its shifted, say
        # that we check the middle element, but instead of a target value, we check a left 
        # or right pointer, if the pointer to the I guess right is lower in value, then we
        # know to go that way because the 'ascending' list must drop to its first value.

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]