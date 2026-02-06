#
# @lc app=leetcode id=3634 lang=python3
#
# [3634] Minimum Removals to Balance Array
#

# @lc code=start
class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()

        if nums[-1] <= nums[0] * k:
            return 0
        
        n = len(nums)

        ans = n - 1

        for i in range(n):
            j = bisect.bisect(nums, nums[i] * k, 0, n)
            ans = min(ans, n - (j - i))

        return ans
        
       
# @lc code=end

