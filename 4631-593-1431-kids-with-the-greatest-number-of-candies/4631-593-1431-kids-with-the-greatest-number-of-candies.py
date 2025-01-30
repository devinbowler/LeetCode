class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        res = []
        for each in candies:
            if each + extraCandies >= maxCandy:
                res.append(True)
            else:
                res.append(False)

        return res
