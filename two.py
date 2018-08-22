# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        carry = 0
        tmp = ListNode(0)
        result = tmp
        while l1 or l2:
            sum = 0
            if l1:
                sum = l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            result.next = ListNode(0)
            result = result.next
            result.val = (int)(sum + carry) % 10
            carry = (int)((sum + carry) / 10)
        if (carry != 0):
            result.next = ListNode(carry)
        return tmp.next