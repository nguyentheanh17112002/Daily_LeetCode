#
# @lc app=leetcode id=2906 lang=python3
#
# [2906] Construct Product Matrix
#

# @lc code=start
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD = 12345
        n, m = len(grid), len(grid[0])
        res = [[1] * m for _ in range(n)]
        flaten = [x for row in grid for x in row]
        prefix = [1] * (n * m)
        suffix = [1] * (n * m)
        
        for i in range(1, n * m):
            prefix[i] = prefix[i - 1] * flaten[i - 1] % MOD
        for i in range(n * m - 2, -1, -1):
            suffix[i] = suffix[i + 1] * flaten[i + 1] % MOD
        for i in range(n):
            for j in range(m):
                idx = i * m + j
                res[i][j] = (prefix[idx] * suffix[idx]) % MOD
        return res

        
# @lc code=end

