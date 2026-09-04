"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        current = head
        mapping = {}

        if not current:
            return None 
        while current:
            mapping[current] = Node(current.val)
            current = current.next

        current = head

        while current:
            copy = mapping[current]
            copy.next = mapping.get(current.next)
            copy.random = mapping.get(current.random)

            current = current.next

        return mapping[head]




