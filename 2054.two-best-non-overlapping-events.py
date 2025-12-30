#
# @lc app=leetcode id=2054 lang=python3
#
# [2054] Two Best Non-Overlapping Events
#

# @lc code=start


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        ans = 0
        events.sort(key = lambda x: x[1])
        ends = [e[1] for e in events]
        bests = [0] * len(events)
        for i in range(len(events)):
            if i == 0:
                bests[i] = events[i][2]
            else:
                bests[i] = max(bests[i - 1], events[i][2])
        for e in events:
            i = bisect_left(ends, e[0]) - 1
            if i >= 0:
                ans = max(ans, e[2] + bests[i])
            else:
                ans = max(ans, e[2])
        return ans



        
# @lc code=end

