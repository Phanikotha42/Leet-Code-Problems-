# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        n1 = ''
        n2 = ''
 
        while l1:
            n1 = str(l1.val) + n1
            l1 = l1.next
 
        while l2:
            n2 = str(l2.val) + n2
            l2 = l2.next
 
        total = int(n1) + int(n2)
 
        dummy = ListNode(0)
        current = dummy
 
        for digit in str(total)[::-1]:
            current.next = ListNode(int(digit))
            current = current.next
 
        return dummy.next