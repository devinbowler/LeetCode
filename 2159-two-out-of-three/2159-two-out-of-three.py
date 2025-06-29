class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        # I think I just make a freqDict and any value that is > 1 I add to
        # the returned array.
        result = []
        
        freqLists = Counter(list(set(nums1)) + list(set(nums2)) + list(set(nums3)))
        for key, value in freqLists.items():
            if value > 1:
                result.append(key)
        
        return result