#
# @lc app=leetcode id=1877 lang=python3
#
# [1877] Minimize Maximum Pair Sum in Array
#

# @lc code=start
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        l = 0
        r = len(nums) - 1
        while(l < r):
            ans = max(ans, nums[l] + nums[r])
            l += 1
            r -= 1
        return ans       
# @lc code=end

