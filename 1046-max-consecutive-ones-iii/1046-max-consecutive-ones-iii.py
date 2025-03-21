class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        st = 0
        en = 0
        flips = 0
        max_count = 0
        run_count = 0
        while(en<len(nums)):
            if(nums[en] == 1):
                en = en+1
                run_count = run_count+1
            elif(flips<k):
                en = en+1
                run_count = run_count+1
                flips = flips+1
            else:
                max_count = max(max_count, run_count)
                flips = flips - (1-nums[st])
                run_count = run_count -1
                st = st+1
        max_count = max(max_count, run_count)
        return max_count
        

        