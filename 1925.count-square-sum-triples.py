#
# @lc app=leetcode id=1925 lang=python3
#
# [1925] Count Square Sum Triples
#

# @lc code=start
class Solution:
    def countTriples(self, n: int) -> int:
        squares = set(i * i for i in range(1, n + 1))
        count = 0

        for a in range(1, n + 1):
            for b in range(a + 1, n + 1):
                c_squared = a * a + b * b
                if c_squared in squares:
                    count += 2  # (a, b, c) and (b, a, c)

        return count
        
# @lc code=end

