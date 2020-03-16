# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if(not root):
            return
        
        ans = []
        s1 = []
        s2 = []

        s1.append(root)

        while(s1):
            x = s1[-1]
            s1.pop()
            s2.append(x)

            if(x.left):
                s1.append(x.left)
            if(x.right):
                s1.append(x.right)
        
        while(s2):
            y = s2[-1]
            s2.pop()
            ans.append(y.val)
        return ans