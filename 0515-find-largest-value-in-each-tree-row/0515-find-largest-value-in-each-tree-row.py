# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        
        out = []
        st = [root]
        if(root is None):
            return []
        child = []
        max_so_far = float("-inf")
        while(len(st) > 0 or len(child) > 0):
            if(len(st) == 0):
                # print("transferign")
                out.append(max_so_far)
                st = child[:]
                max_so_far = float("-inf")
                child = []
            e = st.pop(0)
            # print(e.val, e.left, e.right)
            max_so_far = max(max_so_far, e.val)
            if(e.left):
                child.append(e.left)
            if(e.right):
                child.append(e.right)
        out.append(max_so_far)
        return out