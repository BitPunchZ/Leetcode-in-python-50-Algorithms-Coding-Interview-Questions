# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasSum(self,root,sum,cur):
        if(root is None):
            return False
        cur+=root.val
        if(cur==sum and root.left is None and root.right is None):
            return True
        return (self.hasSum(root.right,sum,cur) or self.hasSum(root.left,sum,cur))
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.hasSum(root,sum, 0)