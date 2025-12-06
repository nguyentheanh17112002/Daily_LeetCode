#
# @lc app=leetcode id=3578 lang=python3
#
# [3578] Count Partitions With Max-Min Difference at Most K
#

# @lc code=start
from collections import deque

class Solution:
    def countPartitions(self, nums, k):
        MOD = 10**9 + 7
        n = len(nums)

        dp = [0] * (n + 1)
        pref = [0] * (n + 1)

        dp[0] = 1
        pref[0] = 1

        maxdq = deque()   
        mindq = deque()   

        l = 0

        for r in range(0, n):
            x = nums[r]

            while maxdq and nums[maxdq[-1]] <= x:
                maxdq.pop()
            maxdq.append(r)

            while mindq and nums[mindq[-1]] >= x:
                mindq.pop()
            mindq.append(r)

            while nums[maxdq[0]] - nums[mindq[0]] > k:
                l += 1
                if maxdq[0] < l:
                    maxdq.popleft()
                if mindq[0] < l:
                    mindq.popleft()

            if l == 0:
                ways = pref[r]
            else:
                ways = (pref[r] - pref[l - 1]) % MOD

            dp[r + 1] = ways
            pref[r + 1] = (pref[r] + ways) % MOD

        return dp[n]


# @lc code=end

