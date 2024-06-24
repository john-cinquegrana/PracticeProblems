# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def tail_recurse(l1, l2, result, carry):
            # Base Case
            if l1 is None and l2 is None and carry==0:
                return
            # Set up the values for addition
            l1_value = 0 if l1 is None else l1.val
            l2_value = 0 if l2 is None else l2.val
            # Set up the pointers for the next run
            l1_next = None if l1 is None else l1.next
            l2_next = None if l2 is None else l2.next
            # Perform the addition
            value = l1_value + l2_value + carry
            new_carry = 1 if value >= 10 else 0
            result.next = ListNode(value % 10)
            return tail_recurse(l1_next, l2_next, result.next, new_carry)
        ll_head = ListNode()
        tail_recurse(l1, l2, ll_head, 0)
        return ll_head.next
        
