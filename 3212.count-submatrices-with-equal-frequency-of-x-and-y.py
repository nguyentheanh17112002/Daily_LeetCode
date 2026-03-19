#
# @lc app=leetcode id=3212 lang=python3
#
# [3212] Count Submatrices With Equal Frequency of X and Y
#

# @lc code=start
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        mp = {
            'X': 1,
            'Y': -1,
            '.': 0
        }
        ans = 0
        contains_X = [[0] * (n + 1) for _ in range(m + 1)]
        prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                contains_X[i][j] = max(mp[grid[i - 1][j - 1]], contains_X[i - 1][j], contains_X[i][j - 1])
                prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + mp[grid[i - 1][j - 1]]
                if contains_X[i][j] == 1 and prefix_sum[i][j] == 0:
                    ans += 1
        return ans
        
# @lc code=end

