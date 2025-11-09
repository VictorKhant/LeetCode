class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        maxDay = days[-1]
        dp = [0] * (maxDay + 1)
        daySet = set(days)

        for i in range(1, maxDay + 1):
            if i not in daySet:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[i - 1] + costs[0], dp[max(0, i - 7)] + costs[1],  dp[max(0, i - 30)] + costs[2])
        
        return dp[maxDay]
        
                
                
