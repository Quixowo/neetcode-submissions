# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(main, other):
            if not main and not other:
                return True
            
            if main and other and main.val == other.val:
                return isSameTree(main.left, other.left) and isSameTree(main.right, other.right)

            return False

        if not root:
            return False
            
        res = isSameTree(root, subRoot)

        if res:
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        