#
# @lc app=leetcode id=2110 lang=python3
#
# [2110] Number of Smooth Descent Periods of a Stock
#

# @lc code=start
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 1
        ans = 0
        smooth_length = 1
        for i in range(1, n):
            if prices[i] + 1 == prices[i - 1]:
                smooth_length += 1
            else:
                ans += (smooth_length * (smooth_length + 1)) // 2
                smooth_length = 1
        ans += (smooth_length * (smooth_length + 1)) // 2
        return ans
        
        
# @lc code=end

