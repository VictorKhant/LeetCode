# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.helper(l1, l2, 0)

    def helper(self, l1, l2, carry):
        if l1 or l2:
            val1, val2 = 0, 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            res = val1 + val2 + carry
            carry = res // 10
            res = res % 10
            return ListNode(res, self.helper(l1, l2, carry))
        elif carry != 0:
            return ListNode(carry)
        return None
        