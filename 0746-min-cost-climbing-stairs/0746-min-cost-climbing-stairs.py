class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        costs = {0:cost[0], 1: cost[1]}
        def dp(c):
            if c not in costs:
                costs[c] = min(dp(c-1), dp(c-2)) + cost[c]
            return costs[c]
        dp(len(cost)-1)
        return costs[len(cost)-1]
