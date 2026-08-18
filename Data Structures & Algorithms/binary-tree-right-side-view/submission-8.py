# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        queue = collections.deque()
        queue.append(root)
        res = []

        while queue:
            level_size = len(queue)
            
            while level_size > 1:
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level_size -= 1
            
            last_node = queue.popleft()
            if last_node.left:
                queue.append(last_node.left)
            if last_node.right:
                queue.append(last_node.right)
            
            res.append(last_node.val)

        return res

