#
# @lc app=leetcode id=3070 lang=python3
#
# [3070] Count Submatrices with Top-Left Element and Sum Less Than k
#

# @lc code=start
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        if grid[0][0] > k:
            return 0
        ans = 0
        m, n = len(grid), len(grid[0])
        acc_sum_matrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                acc_sum_matrix[i][j] = acc_sum_matrix[i - 1][j] + acc_sum_matrix[i][j - 1] - acc_sum_matrix[i - 1][j - 1] + grid[i - 1][j - 1]
                if acc_sum_matrix[i][j] <= k:
                    ans += 1
        return ans       
# @lc code=end

