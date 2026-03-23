#
# @lc app=leetcode id=1594 lang=python3
#
# [1594] Maximum Non Negative Product in a Matrix
#

# @lc code=start
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        max_dp = [[0] * n for _ in range(m)]
        min_dp = [[0] * n for _ in range(m)]
        max_dp[0][0] = min_dp[0][0] = grid[0][0]
        for i in range(1, m):
            max_dp[i][0] = min_dp[i][0] = max_dp[i - 1][0] * grid[i][0]
        for j in range(1, n):
            max_dp[0][j] = min_dp[0][j] = max_dp[0][j - 1] * grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] >= 0:
                    max_dp[i][j] = max(max_dp[i - 1][j], max_dp[i][j - 1]) * grid[i][j]
                    min_dp[i][j] = min(min_dp[i - 1][j], min_dp[i][j - 1]) * grid[i][j]
                else:
                    max_dp[i][j] = min(min_dp[i - 1][j], min_dp[i][j - 1]) * grid[i][j]
                    min_dp[i][j] = max(max_dp[i - 1][j], max_dp[i][j - 1]) * grid[i][j]
        return max_dp[-1][-1] % MOD if max_dp[-1][-1] >= 0 else -1

# @lc code=end

