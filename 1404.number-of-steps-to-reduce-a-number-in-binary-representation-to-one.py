#
# @lc app=leetcode id=1404 lang=python3
#
# [1404] Number of Steps to Reduce a Number in Binary Representation to One
#

# @lc code=start
class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            if s[i] == '1':
                s = s[i:]
                break 
        while s != '1':
            ans += 1
            if s == '0':
                ans += 1
                break
            if s[-1] == '0':
                s = s[:-1]
            else:
                n = len(s)
                for i in range(n-1, -1, -1):
                    if s[i] == '0':
                        s = s[:i] + '1' + s[i+1:]
                        break 
                    else:
                        s = s[:i] + '0' + s[i+1:]
                if i == 0:
                    s = '1' + s
        return ans 
                
            
        
# @lc code=end

