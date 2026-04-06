#
# @lc app=leetcode id=874 lang=python3
#
# [874] Walking Robot Simulation
#

# @lc code=start
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        def add_point(point1, point2):
           return (point1[0] + point2[0], point1[1] + point2[1])
        
        def compute_distance(point):
            return point[0]**2 + point[1]**2

        obstacles = set(tuple(ob) for ob in obstacles)
        cur_direction = 'N'
        transition_mp = {
            'Left': {
                'N': 'W', 
                'W': 'S', 
                'S': 'E', 
                'E': 'N'
            }, 
            'Right': {
               'N': 'E', 
               'E': 'S', 
               'S': 'W', 
               'W': 'N' 
            }
        }
        moves = {
            'N': (0, 1), 
            'E': (1, 0), 
            'S': (0, -1), 
            'W': (-1, 0)
        }
        ans = 0
        cur_pos = (0, 0) 
        for cmd in commands:
            if cmd == -2:
                cur_direction = transition_mp['Left'][cur_direction]
            elif cmd == -1:
                cur_direction = transition_mp['Right'][cur_direction]
            else:
                for _ in range(cmd):
                    move = moves[cur_direction]
                    next_pos = add_point(cur_pos, move)
                    if next_pos in obstacles:
                        break 
                    cur_pos = next_pos
                    dist = compute_distance(cur_pos)
                    ans = max(ans, dist)
        return ans 
        
        
# @lc code=end

