# http://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder

# A class that represents an individual node in a binary tree
class node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


# A function to do pre-order tree traverse
def printPreorder(root):

	# If root exists
	if root:

		# First print the data of node
		print(root.val)

		# then recur on left child
		printPreorder(root.left)

		# now recur on the right child
		printPreorder(root.right)


# A function to do post-order tree traverse
def printPostorder(root):

	if root:

		# First recur on left child
		printPostorder(root.left)

		# then recur on the right child
		printPostorder(root.right)

		# now print the data of the root
		print(root.val)


# A function to do in-order tree traverse
def printInorder(root):

	if root:

		# First recur on the left child
		printInorder(root.left)

		# then print the data of the root
		print(root.val)

		# now recur on the right child
		printInorder(root.right)


# Driver code
root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)


print "Preorder traversal binary tree is"
printPreorder(root)

print "\nInorder traversal binary tree is"
printInorder(root)

print "\nPostorder traversal binary tree is"
printPostorder(root)