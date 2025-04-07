class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dfs(step):
            if step >= len(cost):
                return 0
            return cost[step] + min(dfs(step + 1), dfs(step + 2))

        return min(dfs(0), dfs(1))