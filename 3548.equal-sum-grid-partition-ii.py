#
# @lc app=leetcode id=3548 lang=python3
#
# [3548] Equal Sum Grid Partition II
#

# @lc code=start
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        rows_sum = [sum(row) for row in grid]
        cols_sum = [sum(grid[i][j] for i in range(m)) for j in range(n)]
        total_sum = sum(rows_sum)

        prefix_rows_sum = [0] * m
        prefix_cols_sum = [0] * n

        prefix_rows_sum[0] = rows_sum[0]
        for i in range(1, m):
            prefix_rows_sum[i] = prefix_rows_sum[i - 1] + rows_sum[i]

        prefix_cols_sum[0] = cols_sum[0]
        for j in range(1, n):
            prefix_cols_sum[j] = prefix_cols_sum[j - 1] + cols_sum[j]

        if total_sum % 2 == 0:
            half = total_sum // 2
            for i in range(m - 1):
                if prefix_rows_sum[i] == half:
                    return True
            for j in range(n - 1):
                if prefix_cols_sum[j] == half:
                    return True


        mp = defaultdict(list)
        for i in range(m):
            for j in range(n):
                mp[grid[i][j]].append((i, j))


        for i in range(m - 1):
            top_sum = prefix_rows_sum[i]
            bottom_sum = total_sum - top_sum
            diff = abs(top_sum - bottom_sum)

            if diff == 0:
                return True

            if diff not in mp:
                continue

            if top_sum > bottom_sum:
                for r, c in mp[diff]:
                    if r <= i:
                        height = i + 1
                        width = n

                        if height == 1:
                            if c == 0 or c == n - 1:
                                return True
                        elif width == 1:
                            if r == 0 or r == i:
                                return True
                        else:
                            return True
            else:
                for r, c in mp[diff]:
                    if r > i:
                        height = m - i - 1
                        width = n

                        if height == 1:
                            if c == 0 or c == n - 1:
                                return True
                        elif width == 1:
                            if r == i + 1 or r == m - 1:
                                return True
                        else:
                            return True

        for j in range(n - 1):
            left_sum = prefix_cols_sum[j]
            right_sum = total_sum - left_sum
            diff = abs(left_sum - right_sum)

            if diff == 0:
                return True

            if diff not in mp:
                continue

            if left_sum > right_sum:

                for r, c in mp[diff]:
                    if c <= j:
                        height = m
                        width = j + 1

                        if width == 1:
                            if r == 0 or r == m - 1:
                                return True
                        elif height == 1:
                            if c == 0 or c == j:
                                return True
                        else:
                            return True
            else:

                for r, c in mp[diff]:
                    if c > j:
                        height = m
                        width = n - j - 1

                        if width == 1:
                            if r == 0 or r == m - 1:
                                return True
                        elif height == 1:
                            if c == j + 1 or c == n - 1:
                                return True
                        else:
                            return True

        return False       
        
# @lc code=end

