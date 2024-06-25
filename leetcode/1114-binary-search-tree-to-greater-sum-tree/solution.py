# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def make_greater(root: TreeNode, additive: int) -> int:
            ''' This function will be used to recurse down the tree, changing
            the nodes into GST nodes. It returns the sum of itself plus all of
            its children.'''
            # Base Case
            if root is None:
                return 0
            # Call down the right to get the value of all greater nodes
            right = make_greater(root.right, additive)
            # Save the old root value
            root_value = root.val
            # Update the root value
            gst_value = root_value + additive + right
            root.val = gst_value
            # Call to the left subtree, we put in the additive since we now
            # this node, and everything to the right is greater than the
            # left node.
            left = make_greater(root.left, gst_value)
            # Calculate the return value
            return left + right + root_value
        # Call the make greater function on our root
        make_greater(root, 0)
        # Return the same root since this is in place
        return root
