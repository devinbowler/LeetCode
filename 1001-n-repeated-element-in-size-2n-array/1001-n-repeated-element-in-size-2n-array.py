class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # I think there is an easier way to do this but I have an idea to just
        # use a set to get n + 1, then do a counter and return the key whos value is that

        setNums = set(nums)
        n = len(setNums) - 1
        counterNums = Counter(nums)
        for key, value in counterNums.items():
            if value == n:
                return key