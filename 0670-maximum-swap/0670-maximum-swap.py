class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        import heapq as hq
        a = []
        a = list(str(num))
        dic = []
        n = len(a)
        

        for i in range(n):
            c = a[i]
            hq.heappush(dic, [-1*int(c), -1*i])
        


        i = 0
        d, p = hq.heappop(dic)
        d = d*-1
        p = p*-1
        while(len(dic)>0 and i<n):
            # print(a[i], i, d,p)
            if(p< i):
                # heap is stale, remove that
                d, p = hq.heappop(dic)
                d = d*-1
                p = p*-1
                continue
            elif(str(d) == a[i]):
                #same swap value
                i = i+1
                continue
            else:
                #found valid swap
                a[p], a[i] = a[i], a[p]
                break
        return int("".join(a))

        



        