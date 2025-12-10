#
# @lc app=leetcode id=3583 lang=python3
#
# [3583] Count Special Triplets
#

# @lc code=start
from typing import List
from collections import Counter
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        ans = 0
        freq_next = dict()
        freq_prev = dict()
        mp = dict()
        for i, num in enumerate(nums):
            if num not in mp:
                mp[num] = set()
            mp[num].add(i)
            prev_num = num * 2
            if prev_num in mp:
                if num == 0:
                    freq_prev[i] = len(mp[prev_num]) - 1
                else:
                    freq_prev[i] = len(mp[prev_num])
        
        mp = dict()
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            if num not in mp:
                mp[num] = set()
            mp[num].add(i)
            next_num = num * 2
            if next_num in mp:
                if num == 0:
                    freq_next[i] = len(mp[next_num]) - 1
                else:
                    freq_next[i] = len(mp[next_num])

        for i in range(len(nums)):
            if i in freq_prev and i in freq_next:
                ans = (ans + freq_prev[i] * freq_next[i]) % MOD
        return ans
        
# @lc code=end

