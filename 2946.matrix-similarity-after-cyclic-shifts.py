#
# @lc app=leetcode id=2946 lang=python3
#
# [2946] Matrix Similarity After Cyclic Shifts
#

# @lc code=start
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        def left_shift(row, k):
            k = k % len(row)
            tmp = row[k:] + row[:k]
            return tmp == row
        def right_shift(row, k):
            k = k % len(row)
            tmp = row[-k:] + row[:-k]
            return tmp == row
        for i, row in enumerate(mat):
            if i % 2:
                if not right_shift(row, k):
                    return False
            else:
                if not left_shift(row, k):
                    return False
        return True
# @lc code=end

