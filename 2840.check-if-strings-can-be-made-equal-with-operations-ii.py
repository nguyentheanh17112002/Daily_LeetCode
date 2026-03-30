#
# @lc app=leetcode id=2840 lang=python3
#
# [2840] Check if Strings Can be Made Equal With Operations II
#

# @lc code=start
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        n = len(s1)
        s1_odd = [s1[i] for i in range(1, n, 2)]
        s1_even = [s1[i] for i in range(0, n, 2)]
        s2_odd = [s2[i] for i in range(1, n, 2)]
        s2_even = [s2[i] for i in range(0, n, 2)]
        return sorted(s1_odd) == sorted(s2_odd) and sorted(s1_even) == sorted(s2_even)
# @lc code=end

