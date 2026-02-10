#
# @lc app=leetcode id=3719 lang=python3
#
# [3719] Longest Balanced Subarray I
#

# @lc code=start
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        ans = 0
        for i, num in enumerate(nums):
            mp = {
                "odd": set(), 
                "even": set()
            }
            if num % 2 == 0:
                mp["even"].add(num)
            else:
                mp["odd"].add(num)
            for j in range(i + 1, len(nums)):
                if nums[j] % 2 == 0:
                    mp["even"].add(nums[j])
                else:
                    mp["odd"].add(nums[j])
                if len(mp["even"]) == len(mp["odd"]):
                    ans = max(ans, j - i + 1)
        return ans
        
# @lc code=end

