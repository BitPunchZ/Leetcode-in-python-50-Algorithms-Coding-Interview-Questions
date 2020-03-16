
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


# create root
root = Node(4)

#	    4
#	  /   \
#	None  None


root.left = Node(5)
root.right = Node(6)

# 5 becomes left child and 6 become right child of 1
#		           4
#		       /       \
#		      5	        6
#	      /  \      /   \
#     None None  None  None


root.left.left = Node(7)


# 7 becomes left child of 5
#		           4
#		       /       \
#		      5	        6
#	      /  \      /   \
#      7   None  None  None
#     / \
#  None  None
