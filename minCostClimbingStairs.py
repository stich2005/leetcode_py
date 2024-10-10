#746. Min Cost Climbing Stairs
def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = cost
        for i in range(n-3,-1, -1):            
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        return min(dp[0], dp[1])
