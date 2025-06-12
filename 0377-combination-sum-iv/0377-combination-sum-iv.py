class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # I think this is just a decision tree of sorts, so path finding
        # find everypath that is unique, then increment.
        # A DFS is exponential so its not very efficent so I need like memory.
        memo = {}

        def dfs(current_sum):
            if current_sum in memo:
                return memo[current_sum]
            if current_sum == target:
                return 1
            if current_sum > target:
                return 0
            
            total = 0
            for num in nums:
                total += dfs(current_sum + num)
            memo[current_sum] = total
            return total
            
        return dfs(0)