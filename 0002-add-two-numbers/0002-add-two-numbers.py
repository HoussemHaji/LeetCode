# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        result = ListNode(0)
        sum = result
        while l1 or l2:
            if l1:
                x=l1.val
            else: x = 0
            if l2:
                y=l2.val
            else: y=0
            total = x + y + carry
            carry = total//10
            sum.next = ListNode(total%10)
            sum = sum.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry > 0:
            sum.next = ListNode(carry)
        return result.next