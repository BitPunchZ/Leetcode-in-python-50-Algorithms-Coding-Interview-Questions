# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self,root):
        return 0 if root is None else 1+self.countNodes(root.left)+self.countNodes(root.right)
    def dfs(self,root,k):
        count = self.countNodes(root.left)
        if(count+1==k):
            return root.val
        if(count+1>k):
            return self.dfs(root.left,k)
        if(count+1<k):
            return self.dfs(root.right,k-1-count)
        return -1
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        return self.dfs(root,k)