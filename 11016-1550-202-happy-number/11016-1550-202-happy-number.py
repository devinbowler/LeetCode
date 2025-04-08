class Solution:
    def isHappy(self, n: int) -> bool:
        n = [int(d) for d in str(n)]
        for cycle in range(7):
            totalSum = 0

            for each in n:
                numSquare = each * each
                totalSum += numSquare
            
            if totalSum == 1:
                return True
            else:
                n = [int(d) for d in str(totalSum)]
        
        return False