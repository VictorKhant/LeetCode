class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        maxDay = days[-1]
        dp = [float('inf')] * maxDay
        def minCost(i, n):
            if i < 0 or n < 0:
                return 0
            if days[i] < n:
                return minCost(i, days[i])
            if n < days[i]:
                return minCost(i - 1, n)
            if dp[i] < float('inf'):
                return dp[i]
            cost0 = minCost(i - 1, n - 1) + costs[0]
            cost1 = minCost(i - 1, n - 7) + costs[1]
            cost2 = minCost(i - 1, n - 30) + costs[2]
            dp[i] = min(cost0, cost1, cost2)
            return dp[i]
        return minCost(len(days) - 1, maxDay)
                
                
