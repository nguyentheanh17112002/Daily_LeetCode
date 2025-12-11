#
# @lc app=leetcode id=3531 lang=python3
#
# [3531] Count Covered Buildings
#

# @lc code=start
from typing import List
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        most_left_building = dict()
        most_right_building = dict()
        most_above_building = dict()
        most_below_building = dict()

        for building in buildings:
            x, y = building
            if y not in most_left_building or x < most_left_building[y]:
                most_left_building[y] = x
            if y not in most_right_building or x > most_right_building[y]:
                most_right_building[y] = x
            if x not in most_above_building or y > most_above_building[x]:
                most_above_building[x] = y
            if x not in most_below_building or y < most_below_building[x]:
                most_below_building[x] = y
        ans = 0
        for building in buildings:
            x, y = building
            if x not in most_above_building or x not in most_below_building or y not in most_left_building or y not in most_right_building:
                continue
            if (most_left_building[y] < x < most_right_building[y] and
                most_below_building[x] < y < most_above_building[x]):
                ans += 1

        return ans


        
# @lc code=end

