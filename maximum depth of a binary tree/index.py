# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if(root is None):
            return 0
        if(root.left is None and  root.right is None):
            return 1
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left,right)+1
