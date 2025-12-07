#
# @lc app=leetcode id=1523 lang=python3
#
# [1523] Count Odd Numbers in an Interval Range
#

# @lc code=start
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        low = low if low % 2 != 0 else low + 1
        high = high if high % 2 != 0 else high - 1
        if low > high:
            return 0
        return (high - low) // 2 + 1
        
# @lc code=end

