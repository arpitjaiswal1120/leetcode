"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        current = head

        # First pass: Create a new node after each original node
        while current:
            next_node = current.next
            current.next = Node(current.val)
            current.next.next = next_node
            current = next_node

        # Second pass: Connect random pointers for the copied nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # Third pass: Separate the original and copied lists
        p = head.next
        temp = p
        current = head
        while current and temp:
            current.next = current.next.next if current.next else current.next
            temp.next = temp.next.next if temp.next else temp.next
            current = current.next
            temp = temp.next

        return p
            
        