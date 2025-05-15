# Last updated: 5/14/2025, 9:28:53 PM
# Pretty straight forward backtracking question, just had to watch for using the right variables for the right things. Just check every combo append to a result if it adds to target otherwise pop the last added value.
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # We should just have to loop through 0-9, append until len of path
        # is equal to the value of k, then check if that path = n, if not
        # pop last value and keep looping, if so, add to result and keep going
        # anyway because we want to find all combos.
        result = []

        def backtrack(startPoint, path):
            if len(path) == k:
                if sum(path) == n:
                    result.append(path[:])
                return
            for idx in range(startPoint, 10):
                if idx > n:
                    break
                path.append(idx)
                backtrack(idx + 1, path)
                path.pop()

        backtrack(1, [])
        return result
