#
# @lc app=leetcode id=865 lang=python3
#
# [865] Smallest Subtree with all the Deepest Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return 0, None 
            left_tree_length, left_node = dfs(node.left)
            right_tree_length, right_node = dfs(node.right)

            if left_tree_length > right_tree_length:
                return left_tree_length + 1, left_node
            elif right_tree_length > left_tree_length:
                return right_tree_length + 1, right_node
            else:
                return left_tree_length + 1, node 
        return dfs(root)[1]
    

# @lc code=end

