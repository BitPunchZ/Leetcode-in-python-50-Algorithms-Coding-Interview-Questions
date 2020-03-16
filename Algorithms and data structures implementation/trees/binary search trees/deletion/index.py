

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


def insert(root, node):
    if(root is None):
        root = node
        return

    if(root.data < node.data):
        if(root.right is None):
            root.right = node
        else:
            insert(root.right, node)
    else:
        if(root.left is None):
            root.left = node
        else:
            insert(root.left, node)


def preorder(node):
    if(node is not None):
        print(node.data)
        preorder(node.left)
        preorder(node.right)


def minValueNode(node):
    while(node.left is not None):
        node = node.left
    return node


def deleteNode(node, key):
    if(node is None):
        return node
    # If the key to be deleted is smaller than the node's
    # key then it lies in  left subtree
    if key < node.data:
        node.left = deleteNode(node.left, key)
    # If the kye to be delete is greater than the node's key
    # then it lies in right subtree
    elif(key > node.data):
        node.right = deleteNode(node.right, key)
    # If key is same as node's key, then this is the node
    # to be deleted
    else:
        # Node with only one child or no child
        if node.left is None:
            temp = node.right
            node = None
            return temp
        elif node.right is None:
            temp = node.left
            node = None
            return temp

        # Node with two children: Get the inorder successor
        # (smallest in the right subtree)
        temp = minValueNode(node.right)
        # Copy the inorder successor's content to this node
        node.data = temp.data
        # Delete the inorder successor
        node.right = deleteNode(node.right, temp.data)

    return node


#	           5
#       /  	      \
#     3	            7
#   /   \        /     \
#  2     4      6        8
tree = Node(5)

insert(tree, Node(3))


insert(tree, Node(2))

insert(tree, Node(4))

insert(tree, Node(7))

insert(tree, Node(6))

insert(tree, Node(8))

deleteNode(tree, 7)

#	           5
#       /  	      \
#     3	            8
#   /   \        /     \
#  2     4      6       None


# 5 3 2 4 8 6
preorder(tree)
