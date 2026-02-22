#
# @lc app=leetcode id=868 lang=python3
#
# [868] Binary Gap
#

# @lc code=start
class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]
        cur_1 = 0
        for i, c in enumerate(binary):
            if c == '1':
                cur_1 = i
                break
        ans = 0
        for i in range(cur_1 + 1, len(binary)):
            if binary[i] == '1':
                ans = max(ans, i - cur_1)
                cur_1 = i
        return ans
 
# @lc code=end

