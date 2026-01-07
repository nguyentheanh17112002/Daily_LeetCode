#
# @lc app=leetcode id=1975 lang=python3
#
# [1975] Maximum Matrix Sum
#

# @lc code=start
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        ans = 0
        n = len(matrix)
        neg_cnt = 0
        min_neg = 10**5 + 1

        for row in matrix:
            for num in row:
                if num < 0:
                    neg_cnt += 1
                ans += abs(num)
                min_neg = min(min_neg, abs(num))

        if neg_cnt % 2 == 1:
            ans -= 2 * min_neg
        return ans
# @lc code=end

