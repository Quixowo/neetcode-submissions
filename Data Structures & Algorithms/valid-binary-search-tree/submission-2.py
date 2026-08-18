# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root, lower_range, upper_range):
            if not root:
                return True

            if root.val > lower_range and root.val < upper_range:
                return isValid(root.left, lower_range, root.val) and isValid(root.right, root.val, upper_range)
            else:
                return False

        #when you go left, you put the root val as upper range, 
        #right you put root val as lower range

        return isValid(root, float('-inf'), float('inf'))