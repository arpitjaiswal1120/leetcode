class Solution(object):
    import random
    def __init__(self, w):
        """
        :type w: List[int]
        """
        s = 0
        self.ps = []
        for n in w:
            s = s+n
            self.ps.append(s)
        

    def pickIndex(self):
        """
        :rtype: int
        """
        roll = random.randint(1, self.ps[-1])
        s = 0
        e = len(self.ps)-1
        while(s<=e):
            m = (s+e)/2
            if(roll == self.ps[m]):
                return m
            elif(roll < self.ps[m] ):
                e = m-1
            else:
                s = m+1
        return s


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()