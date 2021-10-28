# Definition for singly-linked list.

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def carry_copy(ls, carry):
            ''' Copy a list while considering a carry from previous addition. '''
            if ls == None:
                if carry == 0:
                    return None
                else: return ListNode(val=carry)
            
            # Perform the arithmetic
            sum = ls.val + carry
            new_carry = 0 if (sum < 10) else 1
            ones_col = sum if (sum < 10) else (sum-10)
            
            #Calculate the later nodes
            next_node = carry_copy(ls.next, new_carry)
            
            return ListNode(val=ones_col, next=next_node)
        
        def add(first, second, carry, acc):
            ''' Recursively add together the two lists, including a carry, into the
            accumulator variable. The accumulator variable points to the end of
            the linked list containing the sum'''
            # Check to see if one list is empty
            if first == None:
                # First list is empty
                # carry_copy takes care of the case when they're both empty
                acc.next = carry_copy( second, carry )
                return
            if second == None:
                acc.next = carry_copy( first, carry )
                return
            # If one list is empty, the sum is simply the other list and the carry
            
            # We are sure both lists have at least one number in them
            # We perform the arithmetic
            sum = first.val + second.val + carry
            new_carry = 0 if (sum < 10) else 1
            ones_col = sum if (sum < 10) else (sum-10)
            
            # Place the next node and iterate
            step = ListNode(val=ones_col)
            acc.next = step
            add(first.next, second.next, new_carry, step)
        
        # Create a dummy head to the sum list
        head = ListNode()
        add(l1, l2, 0, head)
        return head.next
            
