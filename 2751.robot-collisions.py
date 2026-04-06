#
# @lc app=leetcode id=2751 lang=python3
#
# [2751] Robot Collisions
#

# @lc code=start
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        robots = [(positions[i], healths[i], directions[i]) for i in range(n)]
        robots.sort(key=lambda x: x[0])  # Sort by position
        res = []
        idx = 0 
        while(idx < n and robots[idx][2] == 'L'):
            res.append((robots[idx][1], robots[idx][0]))
            idx += 1
        robots = robots[idx:]
        stack = []
        for pos, health, direction in robots:
            if direction == 'R':
                stack.append([health, pos])
            else:
                while stack and health > 0:
                    top = stack[-1]
                    if top[0] < health:
                        stack.pop()
                        health -= 1
                    elif top[0] == health:
                        stack.pop()
                        health = 0
                    else:
                        stack[-1][0] -= 1
                        health = 0
                if health > 0:
                    res.append([health, pos])
        res.extend([[h, p] for h, p in stack])
        mp = {
            p: h for h, p in res
        }
        res = []
        for pos in positions:
            if pos in mp:
                res.append(mp[pos])
        return res
             
        
        
# @lc code=end

