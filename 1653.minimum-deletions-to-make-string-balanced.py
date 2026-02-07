#
# @lc app=leetcode id=1653 lang=python3
#
# [1653] Minimum Deletions to Make String Balanced
#

# @lc code=start
class Solution:
    def minimumDeletions(self, s: str) -> int:
        cnt_a = s.count('a')
        cnt_b = s.count('b')
        if cnt_a == 0 or cnt_b == 0:
            return 0
        n = len(s)
        ans = 10**6
        prefix_b = [0] * (n + 1)
        suffix_a = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_b[i] = prefix_b[i - 1] + (1 if s[i - 1] == 'b' else 0)
        for i in range(n - 1, -1, -1):
            suffix_a[i] = suffix_a[i + 1] + (1 if s[i] == 'a' else 0)
        for i in range(n + 1):
            ans = min(ans, prefix_b[i] + suffix_a[i])
        return ans

# @lc code=end

