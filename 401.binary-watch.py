#
# @lc app=leetcode id=401 lang=python3
#
# [401] Binary Watch
#

# @lc code=start
from itertools import combinations
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        output = []
        hours = [1, 2, 4, 8]
        minutes = [1, 2, 4, 8, 16, 32]

        for i in range(turnedOn + 1):
            for h in combinations(hours, i):
                for m in combinations(minutes, turnedOn - i):
                    hour = sum(h)
                    minute = sum(m)

                    if hour < 12 and minute < 60:
                        output.append(f"{hour}:{minute:02d}")
        return output
# @lc code=end

