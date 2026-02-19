#
# @lc app=leetcode id=696 lang=python3
#
# [696] Count Binary Substrings
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int: 
        ans, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                ans += min(prev, cur)
                prev, cur = cur, 1
        return ans + min(prev, cur)
# @lc code=end

