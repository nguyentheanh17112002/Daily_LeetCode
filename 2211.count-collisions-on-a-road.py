#
# @lc app=leetcode id=2211 lang=python3
#
# [2211] Count Collisions on a Road
#

# @lc code=start
class Solution:
    def countCollisions(self, directions: str) -> int:
        while(directions[0] == 'L'):
            directions = directions[1:]
            if not directions:
                return 0
        while(directions and directions[-1] == 'R'):
            directions = directions[:-1]
            if not directions:
                return 0
        ans = 0
        for d in directions:
            if d != 'S':
                ans += 1
        
        return ans
        
# @lc code=end

