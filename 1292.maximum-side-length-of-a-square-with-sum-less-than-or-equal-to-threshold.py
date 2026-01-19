#
# @lc app=leetcode id=1292 lang=python3
#
# [1292] Maximum Side Length of a Square with Sum Less than or Equal to Threshold
#

# @lc code=start
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        ans = 0
        m, n = len(mat), len(mat[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = (
                    mat[i - 1][j - 1]
                    + prefix[i - 1][j]
                    + prefix[i][j - 1]
                    - prefix[i - 1][j - 1]
                )
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                low, high = 0, min(m - i + 1, n - j + 1)
                while low < high:
                    mid = (low + high + 1) // 2
                    total = (
                        prefix[i + mid - 1][j + mid - 1]
                        - prefix[i - 1][j + mid - 1]
                        - prefix[i + mid - 1][j - 1]
                        + prefix[i - 1][j - 1]
                    )
                    if total <= threshold:
                        low = mid
                    else:
                        high = mid - 1
                ans = max(ans, low)
        return ans
        
# @lc code=end

