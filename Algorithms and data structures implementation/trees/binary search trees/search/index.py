

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


def search(node, key):
    print("Current Node is: ", node.data)
    if(node is None):
        print("No node found")
        return None
    if(node.data == key):
        print("Node found !")
        return node

    if(node.data < key):
        return search(node.right, key)

    return search(node.left, key)


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

search(tree, 8)
