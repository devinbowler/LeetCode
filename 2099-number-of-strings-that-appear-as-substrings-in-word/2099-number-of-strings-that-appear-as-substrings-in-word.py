class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        # Okay so just look through patterns and if the sliding window
        # of that size matches at all increment a return value then break
        # and go to the next pattern?
        count = 0

        for each in patterns:
            if each in word:
                count += 1
        return count