class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start, end, max_length = 0, 0, 0

        while end < len(nums):
            if nums[end] == 0:
                if k > 0:
                    k -= 1
                else:
                    while nums[start] == 1:
                        start += 1
                    start += 1

            max_length = max(max_length, end - start + 1)
            end += 1
                

        return max_length