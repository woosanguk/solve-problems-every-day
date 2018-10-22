"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = []
        carry = 0
        while l1 is not None or l2 is not None:
            x = 0 if l1 is None else l1.val
            y = 0 if l2 is None else l2.val
            sum_val = x + y + carry
            carry = int(sum_val / 10)
            result.append(sum_val % 10)
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry:
            result.append(carry)
        return result


def gen_list_node(input_list):
    result = ListNode(input_list[0])
    first = result
    for index in range(1, len(input_list)):
        first.next = ListNode(input_list[index])
        first = first.next
    return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.addTwoNumbers(gen_list_node([2, 4, 3]), gen_list_node([5, 6, 4])))
    print(solution.addTwoNumbers(gen_list_node([2, 4, 3, 6]), gen_list_node([5, 6, 4])))
    pass
