#
# @lc app=leetcode id=3643 lang=python3
#
# [3643] Flip Square Submatrix Vertically
#

# @lc code=start
class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        high_row, low_row = x, x + k - 1
        while(high_row < low_row):
            for i in range(k):
                grid[high_row][y + i], grid[low_row][y + i] = grid[low_row][y + i], grid[high_row][y + i]
            low_row -= 1
            high_row += 1
        return grid       
# @lc code=end

