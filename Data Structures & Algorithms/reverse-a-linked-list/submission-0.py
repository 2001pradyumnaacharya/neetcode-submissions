# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        perv = None
        while curr:
            ans = ListNode()
            ans.next = perv
            ans.val = curr.val
            perv = ans
            print(f"Adding so the perv {perv.val, perv.next}")
            curr = curr.next
        
        return perv