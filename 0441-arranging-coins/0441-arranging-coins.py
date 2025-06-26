class Solution:
    def arrangeCoins(self, n: int) -> int:
        # This seems like honestly you could solve this with just math, like this is 
        # an algorithms problem for sure. But using DSA I would simply loop while the 
        # row amount is less than or equal to the current amount of n (keep subracting as you go).

        curRow = 0
        while n >= curRow + 1:
            curRow += 1
            n -= curRow
        return curRow