class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        result = 0
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                result = max(result, prices[right] - prices[left])
            right += 1
        return result