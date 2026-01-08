#
# @lc app=leetcode id=1458 lang=python3
#
# [1458] Max Dot Product of Two Subsequences
#

# @lc code=start
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                prod = nums1[i - 1] * nums2[j - 1]
                dp[i][j] = max(
                    prod,
                    dp[i - 1][j - 1] + prod,
                    dp[i - 1][j],
                    dp[i][j - 1]
                )
        
        return dp[n][m]
# @lc code=end

