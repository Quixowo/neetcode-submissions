# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')       
        
        def get_sum(root):
            if not root:
                return 0

            curr_val = root.val
            left_sum = get_sum(root.left)
            if left_sum < 0:
                left_sum = 0
            right_sum = get_sum(root.right)
            if right_sum < 0:
                right_sum = 0

            self.max_sum = max(self.max_sum, curr_val + left_sum + right_sum)

            return curr_val + max(left_sum, right_sum)
        get_sum(root)

        return self.max_sum