# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def zag(stack, acc, direction):
            # Base case
            if len(stack) == 0:
                # This implies the last iteration was all None's, and is an empty list
                return acc[:-1]
            new_stack = []
            current_level = []
            while len(stack) > 0:
                current = stack.pop()
                if current == None:
                    # This happens if there is a missing child
                    continue
                else:
                    # Add the current value
                    current_level.append( current.val)
                    # Add current's children to the stack in proper order
                    if direction == 'right':
                        new_stack.append(current.left)
                    new_stack.append(current.right)
                    if direction == 'left':
                        new_stack.append(current.left)
            # Base Case
            if len(current_level) == 0:
                return acc
            
            # Recursive call
            acc.append(current_level)
            return zag(new_stack, acc, 'left' if (direction=='right') else 'right')
                    
        return zag([root], [], 'right')
        
