# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if(root is None):
            return "X#"

        leftSerialized = self.serialize(root.left)
        rightSerialized = self.serialize(root.right)

        return str(root.val)+"#"+leftSerialized+rightSerialized

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """

        def dfs():
            val = next(data)
            if val == 'X':
                return None
            node = TreeNode(int(val))

            node.left = dfs()
            node.right = dfs()

            return node

        data = iter(data.split("#"))
        return dfs()


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
