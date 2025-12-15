#
# @lc app=leetcode id=2147 lang=python3
#
# [2147] Number of Ways to Divide a Long Corridor
#

# @lc code=start
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        seats = [i for i, c in enumerate(corridor) if c == 'S']
        if len(seats) % 2 != 0:
            return 0
        if len(seats) == 0:
            return 0
        
        ans = 1 
        for i in range(1, len(seats) // 2):
            left = seats[2 * i - 1]
            right = seats[2 * i]
            ans = (ans * (right - left)) % MOD
        return ans
        
# @lc code=end

