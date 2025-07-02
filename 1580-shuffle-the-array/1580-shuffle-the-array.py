class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # Okay so we are given n, and the array is 2n size, so I assume if I just
        # start at n, and start at 0, then alternate making a new array we get our
        # resulting array.
        result = []
        for index in range(n):
            result.append(nums[index])
            result.append(nums[index + n])
        return result