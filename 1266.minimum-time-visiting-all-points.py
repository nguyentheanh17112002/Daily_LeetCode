#
# @lc app=leetcode id=1266 lang=python3
#
# [1266] Minimum Time Visiting All Points
#

# @lc code=start
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points) - 1):
            curr_x, curr_y = points[i]
            target_x, target_y = points[i + 1]
            ans += max(abs(target_x - curr_x), abs(target_y - curr_y))
        
        return ans
# @lc code=end

