#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        bin_respresentation = bin(n)[2:]
        bin_respresentation = bin_respresentation.zfill(32)
        return int(bin_respresentation[::-1], 2)
        
# @lc code=end

