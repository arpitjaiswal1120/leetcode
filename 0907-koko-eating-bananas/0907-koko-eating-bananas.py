class Solution(object):
    import math
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        piles = sorted(piles)
        n = len(piles)
        st = 1
        end = max(piles)
        out = float("inf")
        while(st<=end):
            mid = (st+end)/2
            #print(st, mid, end)
            if(self.calc_hours(piles, mid) <= h):
                # current config able to eat banana
                # reduce k
                end = mid-1
                out = min(out, mid)
            else:
                st = mid+1
        return out



    def calc_hours(self, piles, k):
        h = 0
        for i in piles:
            h = h + math.ceil(1.0*i/k)
        return h
        