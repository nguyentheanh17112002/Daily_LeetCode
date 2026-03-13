#
# @lc app=leetcode id=3296 lang=python3
#
# [3296] Minimum Number of Seconds to Make Mountain Height Zero
#

# @lc code=start
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        ans = 0
        heap = []
        for workerTime in workerTimes:
            heapq.heappush(heap, (workerTime * 1, workerTime, 1))
        while(mountainHeight):
            time, workerTime, turn = heapq.heappop(heap)
            ans = max(ans, time)
            heapq.heappush(heap, (time + workerTime * (turn + 1), workerTime, turn + 1))
            mountainHeight -= 1
        return ans       
# @lc code=end

