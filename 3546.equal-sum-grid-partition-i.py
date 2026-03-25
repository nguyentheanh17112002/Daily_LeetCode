#
# @lc app=leetcode id=3546 lang=python3
#
# [3546] Equal Sum Grid Partition I
#

# @lc code=start
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        row_sums = [sum(row) for row in grid]
        col_sums = [sum(col) for col in zip(*grid)]
        grid_sum = sum(row_sums)
        if grid_sum % 2 != 0:
            return False
        target = grid_sum // 2
        # Check if we can partition rows into two groups with equal sum
        vertical_partition_sum = 0
        horizontal_partition_sum = 0
        for i in range(len(row_sums)):
            vertical_partition_sum += row_sums[i]
            if vertical_partition_sum == target:
                return True
        # Check if we can partition columns into two groups with equal sum
        for i in range(len(col_sums)):
            horizontal_partition_sum += col_sums[i]
            if horizontal_partition_sum == target:
                return True
        return False
# @lc code=end

