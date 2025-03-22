class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        out = []
        for i in range(n):
            for j in range(len(nums[i])):
                out.append([i+j, -1*i, nums[i][j]])
        out = sorted(out)
        return [a[2] for a in out]
