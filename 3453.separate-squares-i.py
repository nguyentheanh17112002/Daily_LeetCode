#
# @lc app=leetcode id=3453 lang=python3
#
# [3453] Separate Squares I
#

# @lc code=start
class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # low_y = float('inf')
        # high_y = float('-inf')
        # epsilon = 1e-6
        # for square in squares:
        #     x, y, l = square
        #     low_y = min(low_y, y)
        #     high_y = max(high_y, y + l)
        # ans = -1.0
        # while(low_y <= high_y):
        #     mid_y = (low_y + high_y) / 2
        #     lower_area = 0
        #     upper_area = 0
        #     for square in squares:
        #         x, y, l = square
        #         if y + l <= mid_y:
        #             lower_area += l * l
        #         elif y >= mid_y:
        #             upper_area += l * l
        #         else:
        #             lower_part = mid_y - y
        #             upper_part = y + l - mid_y
        #             lower_area += lower_part * l
        #             upper_area += upper_part * l
        #     if abs(lower_area - upper_area) <= epsilon:
        #         ans = min(ans, mid_y) if ans != -1.0 else mid_y
        #         high_y = mid_y
        #     elif lower_area < upper_area:
        #         low_y = mid_y 
        #     else:
        #         high_y = mid_y 

        # return ans
        low = min(y for _, y, _ in squares)
        high = max(y + l for _, y, l in squares)

        total = 0.0
        for _, _, l in squares:
            total += float(l) * float(l)
        half = total / 2.0

        def below_area(Y: float) -> float:
            area = 0.0
            for _, y, l in squares:
                if Y <= y:
                    continue
                if Y >= y + l:
                    area += float(l) * float(l)
                else:
                    area += (Y - y) * float(l)
            return area

        eps = 1e-6  # đủ chặt cho yêu cầu 1e-5
        while high - low > eps:
            mid = (low + high) / 2.0
            if below_area(mid) >= half:
                high = mid
            else:
                low = mid

        return high   
# @lc code=end

