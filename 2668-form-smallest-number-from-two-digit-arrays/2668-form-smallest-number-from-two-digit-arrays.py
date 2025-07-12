class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        # I mean is this not just concat the min of both
        for each in sorted(nums1):
            if each in nums2:
                return each
        first, second = min(nums1), min(nums2)
        string1, string2 = str(first) + str(second), str(second) + str(first)
        return min(int(string1), int(string2))