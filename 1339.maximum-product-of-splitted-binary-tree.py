#
# @lc app=leetcode id=1339 lang=python3
#
# [1339] Maximum Product of Splitted Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        # MOD = 10**9 + 7
        # ans = 0
        # def calculate_sum(node):
        #     if not node:
        #         return 0
        #     return node.val + calculate_sum(node.left) + calculate_sum(node.right)
        
        # def find_max_product(node, prev_sum):
        #     nonlocal ans
        #     if not node:
        #         return 
                    
        #     left_sum = calculate_sum(node.left)
        #     right_sum = calculate_sum(node.right)
        #     ans = max(ans, left_sum * (prev_sum + right_sum))
        #     ans = max(ans, right_sum * (prev_sum + left_sum))

        #     if node.left:
        #         find_max_product(node.left, prev_sum + right_sum + node.left.val)
        #     if node.right:
        #         find_max_product(node.right, prev_sum + left_sum + node.right.val)
        #     return 

        # find_max_product(root, root.val)
        # return ans % MOD

        MOD = 10**9 + 7
        ans = 0
        subtree_sums = []
        
        def dfs(node):
            if not node:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            current_sum = node.val + left_sum + right_sum
            subtree_sums.append(current_sum)
            return current_sum
        
        total_sum = dfs(root)
        
        for subtree_sum in subtree_sums:
            ans = max(ans, subtree_sum * (total_sum - subtree_sum))
        
        return ans % MOD
# @lc code=end

