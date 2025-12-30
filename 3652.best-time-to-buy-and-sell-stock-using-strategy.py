#
# @lc app=leetcode id=3652 lang=python3
#
# [3652] Best Time to Buy and Sell Stock using Strategy
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        ans = 0
        n = len(prices)
        original_prefix_sum = [0] * (n + 1)
        sell_prefix_sum = [0] * (n + 1)
        
        original_prefix_sum[0] = prices[0] * strategy[0]
        sell_prefix_sum[0] = prices[0] * 1

        for i in range(1, n):
            original_prefix_sum[i] = prices[i]*strategy[i] + original_prefix_sum[i-1]
            sell_prefix_sum[i] = prices[i]*1 + sell_prefix_sum[i-1]
        
        ans = original_prefix_sum[-1]
        for i in range(n - k + 1):
            first_original_part = original_prefix_sum[i - 1] if i > 0 else 0
            hold_part = 0
            sell_part = sell_prefix_sum[i + k - 1] - sell_prefix_sum[i + k // 2 - 1]
            last_original_part = original_prefix_sum[-1] - original_prefix_sum[i + k - 1]
            ans = max(ans, first_original_part + hold_part + sell_part + last_original_part)
        return ans

        
# @lc code=end

