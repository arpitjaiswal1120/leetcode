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
        node_dict = {}
        if(head is None):
            return None
        node_dict[head] =  Node(head.val)

        t = head
        while(t):
            
            if(t.next is None):
                # print(t.val, t.next, "skipping")
                pass
            elif(t.next in node_dict):
                # print(t.val, t.next.val, "assigning")
                node_dict[t].next = node_dict[t.next]
            else:
                # print(t.val, t.next.val, "creating and assigning")
                node_dict[t.next] =  Node(t.next.val)
                node_dict[t].next = node_dict[t.next]
            
            if(t.random is None):
                pass
            elif(t.random in node_dict):
                node_dict[t].random = node_dict[t.random]
            else:
                node_dict[t.random] =  Node(t.random.val)
                node_dict[t].random = node_dict[t.random]
            
            t = t.next
        return node_dict[head]
            
        