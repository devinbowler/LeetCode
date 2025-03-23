class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        for each in nums1:
            if each in nums2:
                res.append(each)
                delete = nums2.index(each)
                del nums2[delete]

        return res