# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode(0)
        result_tail = l3
        buf = 0

        while l1 or l2 or buf:
            value1 = (l1.val if l1 else 0)
            value2 = (l2.val if l2 else 0)
            buf, main_value = divmod(value1 + value2 + buf, 10)

            result_tail.next = listNode(main_value)
            result_tail = result_tail.next

            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
        return l3.next