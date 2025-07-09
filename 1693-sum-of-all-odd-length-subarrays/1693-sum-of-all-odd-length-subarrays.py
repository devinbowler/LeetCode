class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # I could just do a window ig for each odd length, and if its not longer than the actual array
        # just add the sum to a total
        totalSum = 0
        windowSize = 1

        while windowSize <= len(arr):
            for idx in range(len(arr) - (windowSize - 1)):
                print(arr[idx:idx + windowSize])
                totalSum += sum(arr[idx:idx + windowSize])
            windowSize += 2
        
        return totalSum