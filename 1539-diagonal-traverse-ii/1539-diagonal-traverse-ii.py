class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        from collections import deque
        n = len(nums)
        ans = []
        q = deque([(0,0)])
        while(q):
            r,c = q.popleft()
            ans.append(nums[r][c])
            if(c==0) and r+1<n and c<len(nums[r+1]):
                q.append([r+1, c])
            if(c+1 < len(nums[r])):
                q.append([r, c+1])
            
        return ans
