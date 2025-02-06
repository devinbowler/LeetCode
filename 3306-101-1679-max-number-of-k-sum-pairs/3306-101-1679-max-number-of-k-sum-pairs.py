class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        maxOps = 0

        while nums[right] >= k and right > 0:
            right -= 1

        while left < right:
            val = nums[left] + nums[right]
            if val == k:
                maxOps += 1
                left +=1 
                right -=1
            elif val < k:
                left += 1
            else:
                right -= 1

        return maxOps