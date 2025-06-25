class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Little bit confusing wording but I think its just go through nums1, and
        # for each number in that check nums2, and return either the number to the right
        # if greater or return -1. Oh keep going actually not just immediate right.
        returnArray = []

        for each in nums1:
            index = nums2.index(each)

            for idx in range(index + 1, len(nums2)):
                if nums2[idx] > each:
                    returnArray.append(nums2[idx])
                    break
            else:
                returnArray.append(-1)

        return returnArray