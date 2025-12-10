#
# @lc app=leetcode id=3577 lang=python3
#
# [3577] Count the Number of Computer Unlocking Permutations
#

# @lc code=start
class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10**9 + 7
        root_complexity = complexity[0]
        for i in range(1, len(complexity)):
            if complexity[i] <= root_complexity:
                return 0
        ans = 1
        for i in range(1, len(complexity)):
            ans = ans * i % MOD
        return ans
# @lc code=end

