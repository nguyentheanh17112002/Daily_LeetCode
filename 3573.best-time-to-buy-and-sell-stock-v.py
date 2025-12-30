#
# @lc app=leetcode id=3573 lang=python3
#
# [3573] Best Time to Buy and Sell Stock V
#

# @lc code=start
class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        NEG = -10**30
        
        flat = [NEG] * (k + 1)
        long = [NEG] * (k + 1)
        short = [NEG] * (k + 1)
        flat[0] = 0

        for p in prices:
            nflat = flat[:]    
            nlong = long[:]
            nshort = short[:]

            for t in range(k + 1):

                if flat[t] != NEG:
                    nlong[t] = max(nlong[t], flat[t] - p)
                    nshort[t] = max(nshort[t], flat[t] + p)

                if t + 1 <= k:
                    if long[t] != NEG:
                        nflat[t + 1] = max(nflat[t + 1], long[t] + p)
                    if short[t] != NEG:
                        nflat[t + 1] = max(nflat[t + 1], short[t] - p)

            flat, long, short = nflat, nlong, nshort

        return max(flat)   
# @lc code=end

