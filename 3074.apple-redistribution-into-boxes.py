#
# @lc app=leetcode id=3074 lang=python3
#
# [3074] Apple Redistribution into Boxes
#

# @lc code=start
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        if sum(capacity) < total_apples:
            return -1
        capacity.sort(reverse=True)
        boxes_used = 0
        for cap in capacity:
            if total_apples <= 0:
                break
            total_apples -= cap
            boxes_used += 1
        return boxes_used
        
# @lc code=end

