#
# @lc app=leetcode id=2483 lang=python3
#
# [2483] Minimum Penalty for a Shop
#

# @lc code=start
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        open_penalty = [0] * (n + 1)
        close_penalty = [0] * (n + 1)

        if customers[0] == 'Y':
            open_penalty[0] = 1
        else:
            close_penalty[0] = 1
        for i in range(1, n):
            open_penalty[i] = open_penalty[i - 1]
            close_penalty[i] = close_penalty[i - 1]
            if customers[i] == 'Y':
                open_penalty[i] += 1
            else:
                close_penalty[i] += 1

        min_penalty = open_penalty[n - 1]
        ans = 0

        for i in range(1, n + 1):
            penalty = close_penalty[i - 1] + (open_penalty[n - 1] - open_penalty[i - 1])
            if penalty < min_penalty:
                min_penalty = penalty
                ans = i
        return ans
        

        
# @lc code=end

