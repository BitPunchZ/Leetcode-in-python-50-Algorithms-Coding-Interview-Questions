# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    ans = -float("inf")
    def solution(self,node):
        if(node is None):
            return 0
        left = self.solution(node.left)
        right = self.solution(node.right)

        mxSide = max(node.val,max(left,right)+node.val)
        mxTop = max(mxSide,left+right+node.val)
        self.ans = max(self.ans,mxTop)
        return mxSide

    def maxPathSum(self, root: TreeNode) -> int:
        self.solution(root)
        return self.ans
