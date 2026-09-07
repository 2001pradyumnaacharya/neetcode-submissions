# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = ""
        b = ""
        c = ListNode()
        dummy = c

        while l1:
            a = a + str(l1.val)
            l1 = l1.next

        while l2:
            b = b + str(l2.val)
            l2 = l2.next

        c = str(int(a[::-1]) + int(b[::-1]))
        dummy = ListNode()
        current = dummy

        for i in c[::-1]:
            current.next = ListNode(int(i))
            current = current.next

        return dummy.next
            
        
