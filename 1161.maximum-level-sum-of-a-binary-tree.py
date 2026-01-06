#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        mp = dict()
        
        def traverse(node, level):
            if level not in mp:
                mp[level] = 0
            mp[level] += node.val

            if node.left:
                traverse(node.left, level + 1)
            if node.right:
                traverse(node.right, level + 1)
            return 
        
        traverse(root, 1)
        max_val = -10**9
        min_level = 1

        for level, val in mp.items():
            if val > max_val:
                max_val = val
                min_level = level
            elif val == max_val:
                if level < min_level:
                    min_level = level
        
        return min_level
        
        
# @lc code=end

