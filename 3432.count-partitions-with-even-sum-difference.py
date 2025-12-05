#
# @lc app=leetcode id=3432 lang=python3
#
# [3432] Count Partitions with Even Sum Difference
#

# @lc code=start
from typing import List
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        ans = 0
        for num in nums[:-1]:
            left_sum += num
            right_sum = total_sum - left_sum
            if left_sum % 2 == right_sum % 2:
                ans += 1
        return ans
# @lc code=end
